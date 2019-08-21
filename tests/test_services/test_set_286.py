# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
import pytest
import logging
from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)
scenario = utest.Scenario(286)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_286(client, variables):
    scenario.initial(variables)
    scenario.variables["UDiskType"] = "DataDisk"
    scenario.variables["Size"] = 1
    scenario.variables["UDataArkMode"] = "No"
    scenario.variables["UDiskName"] = "auto_udisk_noArk"
    scenario.variables["UDiskCloneName"] = "auto_udisk_noArk_Clone"
    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDiskPrice",
)
def describe_udisk_price_00(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": variables.get("UDataArkMode"),
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 1,
        "DiskType": variables.get("UDiskType"),
        "ChargeType": "Month",
    }
    try:
        resp = client.udisk().describe_udisk_price(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CheckUDiskAllowanceResponse"),
    ],
    action="CheckUDiskAllowance",
)
def check_udisk_allowance_01(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Size": 10,
        "Region": variables.get("Region"),
    }
    try:
        resp = client.invoke("CheckUDiskAllowance", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=1,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUDisk",
)
def create_udisk_02(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": variables.get("UDataArkMode"),
        "Tag": "test",
        "Size": variables.get("Size"),
        "Region": variables.get("Region"),
        "Quantity": 0,
        "Name": variables.get("UDiskName"),
        "DiskType": variables.get("UDiskType"),
        "ChargeType": "Month",
    }
    try:
        resp = client.udisk().create_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["udisk_noArk_id"] = utest.value_at_path(resp, "UDiskId.0")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Status", "Available"),
        ("str_eq", "DataSet.0.Tag", "test"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_03(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CloneUDiskResponse"),
    ],
    action="CloneUDisk",
)
def clone_udisk_04(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "SourceId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
        "Quantity": 0,
        "Name": variables.get("UDiskCloneName"),
        "ChargeType": "Month",
    }
    try:
        resp = client.udisk().clone_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["udisk_noArk_id_clone"] = utest.value_at_path(resp, "UDiskId.0")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDiskUpgradePrice",
)
def describe_udisk_upgrade_price_05(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDataArkMode": variables.get("UDataArkMode"),
        "SourceId": variables.get("udisk_noArk_id"),
        "Size": variables.get("Size") + 1,
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().describe_udisk_upgrade_price(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=80,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ResizeUDisk",
)
def resize_udisk_06(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Size": variables.get("Size") + 1,
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().resize_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.Size", variables.get("Size") + 1),
    ],
    action="DescribeUDisk",
)
def describe_udisk_07(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=40,
    retry_interval=3,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUDiskResponse"),
        ("str_eq", "DataSet.0.Status", "Available"),
    ],
    action="DescribeUDisk",
)
def describe_udisk_08(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id_clone"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteUDisk",
)
def delete_udisk_09(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().delete_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=20,
    retry_interval=3,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDisk",
)
def describe_udisk_10(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteUDiskResponse"),
    ],
    action="DeleteUDisk",
)
def delete_udisk_11(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id_clone"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().delete_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=20,
    retry_interval=3,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUDisk",
)
def describe_udisk_12(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "UDiskId": variables.get("udisk_noArk_id_clone"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.udisk().describe_udisk(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp