# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
import pytest
import logging
from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)
scenario = utest.Scenario(2377)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_2377(client, variables):
    scenario.initial(variables)
    scenario.variables["Password"] = "YW4mODE1MDI5"
    scenario.variables["Type"] = "GPU-2080-V5"
    scenario.variables["ModifyName"] = "TestName"
    scenario.variables["ModifyRemark"] = "TestRemark"
    scenario.variables["Cluster"] = "10G"
    scenario.variables["Raid"] = "NoRaid"
    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribePHostImageResponse"),
    ],
    action="DescribePHostImage",
)
def describe_phost_image_00(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "ImageType": "Base",
    }
    try:
        resp = client.uphost().describe_phost_image(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["ImageID1"] = utest.value_at_path(resp, "ImageSet.0.ImageId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribePHostMachineTypeResponse"),
    ],
    action="DescribePHostMachineType",
)
def describe_phost_machine_type_01(client, variables):
    d = {"Zone": variables.get("Zone"), "Region": variables.get("Region")}
    try:
        resp = client.invoke("DescribePHostMachineType", d)
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
        ("str_eq", "Action", "DescribePHostResourceInfoResponse"),
    ],
    action="DescribePHostResourceInfo",
)
def describe_phost_resource_info_02(client, variables):
    d = {"Zone": variables.get("Zone"), "Region": variables.get("Region")}
    try:
        resp = client.invoke("DescribePHostResourceInfo", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CreatePHostResponse"),
    ],
    action="CreatePHost",
)
def create_phost_03(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Type": variables.get("Type"),
        "Region": variables.get("Region"),
        "Raid": variables.get("Raid"),
        "Password": variables.get("Password"),
        "ImageId": variables.get("ImageID1"),
        "Cluster": variables.get("Cluster"),
    }
    try:
        resp = client.uphost().create_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["phostId"] = utest.value_at_path(resp, "PHostId.0")
    return resp


@scenario.step(
    max_retries=120,
    retry_interval=30,
    startup_delay=20,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribePHostResponse"),
        ("str_eq", "PHostSet.0.PMStatus", "Running"),
    ],
    action="DescribePHost",
)
def describe_phost_04(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": [variables.get("phostId")],
    }
    try:
        resp = client.uphost().describe_phost(d)
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
        ("str_eq", "Action", "GetPHostKVMInfoResponse"),
    ],
    action="GetPHostKVMInfo",
)
def get_phost_kvm_info_05(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": variables.get("phostId"),
    }
    try:
        resp = client.invoke("GetPHostKVMInfo", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "ModifyPHostInfoResponse"),
    ],
    action="ModifyPHostInfo",
)
def modify_phost_info_06(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Remark": variables.get("ModifyRemark"),
        "Region": variables.get("Region"),
        "PHostId": variables.get("phostId"),
        "Name": variables.get("ModifyName"),
    }
    try:
        resp = client.uphost().modify_phost_info(d)
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
        ("str_eq", "Action", "DescribePHostResponse"),
        ("str_eq", "PHostSet.0.Name", variables.get("ModifyName")),
        ("str_eq", "PHostSet.0.Remark", variables.get("ModifyRemark")),
    ],
    action="DescribePHost",
)
def describe_phost_07(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": [variables.get("phostId")],
    }
    try:
        resp = client.uphost().describe_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=10,
    startup_delay=10,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "StopPHostResponse"),
    ],
    action="StopPHost",
)
def stop_phost_08(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": variables.get("phostId"),
    }
    try:
        resp = client.invoke("StopPHost", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=30,
    retry_interval=30,
    startup_delay=10,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribePHostResponse"),
        ("str_eq", "PHostSet.0.PMStatus", "Stopped"),
    ],
    action="DescribePHost",
)
def describe_phost_09(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": [variables.get("phostId")],
    }
    try:
        resp = client.uphost().describe_phost(d)
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
        ("str_eq", "Action", "ReinstallPHostResponse"),
    ],
    action="ReinstallPHost",
)
def reinstall_phost_10(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "Password": variables.get("Password"),
        "PHostId": variables.get("phostId"),
        "ImageId": variables.get("ImageID1"),
    }
    try:
        resp = client.uphost().reinstall_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=120,
    retry_interval=60,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribePHostResponse"),
        ("str_eq", "PHostSet.0.PMStatus", "Running"),
    ],
    action="DescribePHost",
)
def describe_phost_11(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": [variables.get("phostId")],
    }
    try:
        resp = client.uphost().describe_phost(d)
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
        ("str_eq", "Action", "PoweroffPHostResponse"),
    ],
    action="PoweroffPHost",
)
def poweroff_phost_12(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": variables.get("phostId"),
    }
    try:
        resp = client.uphost().poweroff_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=120,
    retry_interval=60,
    startup_delay=0,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribePHostResponse"),
        ("str_eq", "PHostSet.0.PMStatus", "Stopped"),
    ],
    action="DescribePHost",
)
def describe_phost_13(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": [variables.get("phostId")],
    }
    try:
        resp = client.uphost().describe_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=120,
    retry_interval=30,
    startup_delay=20,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "StartPHostResponse"),
    ],
    action="StartPHost",
)
def start_phost_14(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": variables.get("phostId"),
    }
    try:
        resp = client.uphost().start_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=120,
    retry_interval=30,
    startup_delay=20,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribePHostResponse"),
        ("str_eq", "PHostSet.0.PMStatus", "Running"),
    ],
    action="DescribePHost",
)
def describe_phost_15(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": [variables.get("phostId")],
    }
    try:
        resp = client.uphost().describe_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "TerminatePHostResponse"),
    ],
    action="TerminatePHost",
)
def terminate_phost_16(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Region": variables.get("Region"),
        "PHostId": variables.get("phostId"),
    }
    try:
        resp = client.uphost().terminate_phost(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp