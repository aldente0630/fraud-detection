import multiprocessing
import pickle
import botocore
import boto3
import numpy as np
import pandas as pd


def _cast_data_type(series):
    column_type = series.dtype
    if column_type != np.object:
        val_min = series.min()
        val_max = series.max()
        if column_type == np.int_:
            if val_min > np.iinfo(np.int8).min and val_max < np.iinfo(np.int8).max:
                series = series.astype(np.int8)
            elif val_min > np.iinfo(np.int16).min and val_max < np.iinfo(np.int16).max:
                series = series.astype(np.int16)
            elif val_min > np.iinfo(np.int32).min and val_max < np.iinfo(np.int32).max:
                series = series.astype(np.int32)
            elif val_min > np.iinfo(np.int64).min and val_max < np.iinfo(np.int64).max:
                series = series.astype(np.int64)
        else:
            if (
                val_min > np.finfo(np.float16).min
                and val_max < np.finfo(np.float16).max
            ):
                series = series.astype(np.float16)
            elif (
                val_min > np.finfo(np.float32).min
                and val_max < np.finfo(np.float32).max
            ):
                series = series.astype(np.float32)
            else:
                series = series.astype(np.float64)
    return series


def check_bucket_permission(bucket):
    permission = False
    try:
        boto3.Session().client("s3").head_bucket(Bucket=bucket)
    except botocore.exceptions.ParamValidationError:
        print(
            "Hey! You either forgot to specify your S3 bucket \
            or you gave your bucket an invalid name!"
        )
    except botocore.exceptions.ClientError as error:
        if error.response["Error"]["Code"] == "403":
            print(f"Hey! You don't have permission to access the bucket, {bucket}.")
        elif error.response["Error"]["Code"] == "404":
            print(f"Hey! Your bucket, {bucket}, doesn't exist!")
        else:
            raise
    else:
        permission = True
    return permission


def dump_pickle(file_path, obj):
    with open(file_path, "wb") as file:
        pickle.dump(obj, file)


def get_cpu_count(cpu_usage):
    return round(cpu_usage * multiprocessing.cpu_count())


def load_pickle(file_path):
    with open(file_path, "rb") as file:
        obj = pickle.load(file)
    return obj


def reduce_mem_usage(df):
    mem_usage = df.memory_usage().sum() / 1024 ** 2
    print(f"Memory usage of dataframe is {mem_usage:0.2f} MB.")
    df = df.apply(_cast_data_type)
    opt_mem_usage = df.memory_usage().sum() / 1024 ** 2
    print(f"Memory usage after optimization is {opt_mem_usage:0.2f} MB.")
    print(f"Decreased by {(100 * (mem_usage - opt_mem_usage) / mem_usage):0.2f}%.")
    return df


def str_to_int(x):
    return x if pd.isnull(x) else str(int(x))
