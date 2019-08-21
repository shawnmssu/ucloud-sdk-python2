# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
import pytest
import logging
from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)
scenario = utest.Scenario(2457)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_2457(client, variables):
    scenario.initial(variables)
    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateVPC",
)
def create_vpc_00(client, variables):
    d = {
        "Region": variables.get("Region"),
        "Network": ["192.168.0.0/16"],
        "Name": "ulb-ssl-vpc",
    }
    try:
        resp = client.vpc().create_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["vpc_id"] = utest.value_at_path(resp, "VPCId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSubnet",
)
def create_subnet_01(client, variables):
    d = {
        "VPCId": variables.get("vpc_id"),
        "SubnetName": "ulb-ssl-subnet",
        "Subnet": "192.168.111.0",
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().create_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["subnet_id"] = utest.value_at_path(resp, "SubnetId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateULB",
)
def create_ulb_02(client, variables):
    d = {
        "VPCId": variables.get("vpc_id"),
        "ULBName": "ulb-ssl-test",
        "Tag": "Default",
        "SubnetId": variables.get("subnet_id"),
        "Region": variables.get("Region"),
        "InnerMode": "No",
        "ChargeType": "Dynamic",
    }
    try:
        resp = client.ulb().create_ulb(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["ULBId"] = utest.value_at_path(resp, "ULBId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateVServer",
)
def create_vserver_03(client, variables):
    d = {
        "VServerName": "vserver-test",
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
        "Protocol": "HTTPS",
        "PersistenceType": "UserDefined",
        "PersistenceInfo": "huangchao",
        "Method": "Roundrobin",
        "ListenType": "RequestProxy",
        "FrontendPort": 443,
        "ClientTimeout": 60,
    }
    try:
        resp = client.ulb().create_vserver(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["VServerId"] = utest.value_at_path(resp, "VServerId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSSL",
)
def create_ssl_04(client, variables):
    d = {
        "UserCert": """-----BEGIN CERTIFICATE-----
MIIFzTCCBLWgAwIBAgIQQ8IswmAhEIKfNhrKqb0F3DANBgkqhkiG9w0BAQsFADCB
lzELMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMs
IEluYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsT
FERvbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NM
IENBIC0gRzUwHhcNMTYxMjA2MDAwMDAwWhcNMTcxMjA2MjM1OTU5WjAgMR4wHAYD
VQQDDBVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQDxBsuwGdCZdEUs40SQcvUt+9hlmLTgcfkq/h9f1QVPxLq/PC+O
sG76hOgy6N8f7k7x5XgtPKi9O4ydFl8ViYhEXRjYQcUrTm3lu7s9UT2AIUmK0dI+
PZgFU5gDwh8fQLoL24T2lPfkD9TngCnDanfo3xbx/e9hsJkf7hKWix8zrxtYYCUT
t96pTpQeWjr7ggl2bDEfTayJNM+i5xoGBPiQFdxPnKWCjNmXi2dws0d2whi1euRW
gI5wIXji5WKfUf6EvzG0Uzz6i8vsSLGv8pL7C0AuUI4MrPNDesFeA2LEYclQkpHE
E49BkpQvCokCW9d8/r5ASUry+7SrJIncU6FxAgMBAAGjggKJMIIChTAgBgNVHREE
GTAXghVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wCQYDVR0TBAIwADBhBgNVHSAEWjBY
MFYGBmeBDAECATBMMCMGCCsGAQUFBwIBFhdodHRwczovL2Quc3ltY2IuY29tL2Nw
czAlBggrBgEFBQcCAjAZDBdodHRwczovL2Quc3ltY2IuY29tL3JwYTAfBgNVHSME
GDAWgBRtWMd/GufhPy6mjJc1Qrv00zisPzAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0l
BBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMIGbBggrBgEFBQcBAQSBjjCBizA8Bggr
BgEFBQcwAYYwaHR0cDovL3RydXN0YXNpYTItb2NzcC5kaWdpdGFsY2VydHZhbGlk
YXRpb24uY29tMEsGCCsGAQUFBzAChj9odHRwOi8vdHJ1c3Rhc2lhMi1haWEuZGln
aXRhbGNlcnR2YWxpZGF0aW9uLmNvbS90cnVzdGFzaWFnNS5jcnQwggEDBgorBgEE
AdZ5AgQCBIH0BIHxAO8AdQDd6x0reg1PpiCLga2BaHB+Lo6dAdVciI09EcTNtuy+
zAAAAVjT7zdSAAAEAwBGMEQCIDCzWufc1q7hjmrrCetGyoA8EsEqpRSIhmZXStX5
8b7zAiA6x5aAaDK+yMyeAgw71yi3tRVrWayHN+W0+4BxC8u5UQB2AO5Lvbd1zmC6
4UJpH6vhnmajD35fsHLYgwDEe4l6qP3LAAABWNPvN4kAAAQDAEcwRQIgZ/LNgg7n
7AE4O2yZkrXNcqAOmJ3NU2nT6zcnBxPFTTsCIQCjyPbMfWMZTD3kxgxPQ1COw5zJ
sM0dfNmSr3MiU7EhqDANBgkqhkiG9w0BAQsFAAOCAQEAeyfgUhg9ZWVCaz0f+BQU
6fMMfmQ1BDzvVFu+ORoAqyJQogxwIdfjrlz/63YFee5qpUsW/aaz4ma3bb4dpE1K
GsgYe5N3o0xybYlOj+KB61sufYkzQS3HgDevCwjfUlGEbNl4dpO2xh5s5AANXlnz
s/X0+AJ33/bm+fWIjAbIjluaEoM6GETHTXi4Tlxy0j3nsXsB9tIIUibAdTtButef
JJRnikGRN+eHjrsLYe0RUmdKOQz1ik6teHt0MQX0aCe8OlXeyGDd9m8u7+y0nAnH
TVaNuT7vXMWyyXLVUcV898wkBo3Bo3hUiaw0QR0ttgDrf5ZwqPfqpytRW2K5GMZT
uw==
-----END CERTIFICATE-----


-----BEGIN CERTIFICATE-----
MIIFZTCCBE2gAwIBAgIQOhAOfxCeGsWcxf/2QNXkQjANBgkqhkiG9w0BAQsFADCB
yjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL
ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp
U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW
ZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0
aG9yaXR5IC0gRzUwHhcNMTYwODExMDAwMDAwWhcNMjYwODEwMjM1OTU5WjCBlzEL
MAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMsIElu
Yy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsTFERv
bWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NMIENB
IC0gRzUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC39aSJZG/97x3a
6Qmuc9+MubagegRAVUmFYHTYTs8IKB2pM7wXN7W8mekdZaEgUjDFxvRBK/DhTb7U
8ONLsKKdT86aOhzbz2noCTn9wPWnGwkg+/4YKg/dPQQdV9tMsSu0cwqInWHxSAkm
AI1hYFC9D7Sf7Hp/5cRcD+dK454YMRzNOGLQnCVI8JEqrz6o9SOvQNTqTcfqt6DC
0UlXG+MPD1eNPjlzf1Vwaab+VSTgySoC+Ikbq2VsdykeOiGXW/OIiASH7+2LcR05
PmQ7GEOlM8yzoVojFpM8sHz+WxI05ZOPri5+vX3HhHHjWr5432G0dVmgohnZvlVZ
oy8XrlbpAgMBAAGjggF2MIIBcjASBgNVHRMBAf8ECDAGAQH/AgEAMC8GA1UdHwQo
MCYwJKAioCCGHmh0dHA6Ly9zLnN5bWNiLmNvbS9wY2EzLWc1LmNybDAOBgNVHQ8B
Af8EBAMCAQYwLgYIKwYBBQUHAQEEIjAgMB4GCCsGAQUFBzABhhJodHRwOi8vcy5z
eW1jZC5jb20wYQYDVR0gBFowWDBWBgZngQwBAgEwTDAjBggrBgEFBQcCARYXaHR0
cHM6Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYBBQUHAgIwGRoXaHR0cHM6Ly9kLnN5
bWNiLmNvbS9ycGEwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMCkGA1Ud
EQQiMCCkHjAcMRowGAYDVQQDExFTeW1hbnRlY1BLSS0yLTYwMTAdBgNVHQ4EFgQU
bVjHfxrn4T8upoyXNUK79NM4rD8wHwYDVR0jBBgwFoAUf9Nlp8Ld7LvwMAnzQzn6
Aq8zMTMwDQYJKoZIhvcNAQELBQADggEBABUphhBbeG7scE3EveIN0dOjXPgwgQi8
I2ZAKYm6DawoGz1lEJVdvFmkyMbP973X80b7mKmn0nNbe1kjA4M0O0hHaMM1ZaEv
7e9vHEAoGyysMO6HzPWYMkyNxcCV7Nos2Uv4RvLDpQHh7P4Kt6fUU13ipcynrtQD
1lFUM0yoTzwwFsPu3Pk+94hL58ErqwqJQwxoHMgLIQeMVHeNKcWFy1bddSbIbCWU
Zs6cMxhrra062ZCpDCbxyEaFNGAtYQMqNz55Z/14XgSUONZ/cJTns6QKhpcgTOwB
fnNzRnk+aWreP7osKhXlz4zs+llP7goBDKFOMMtoEXx3YjJCKgpqmBU=
-----END CERTIFICATE-----""",
        "SSLName": "证书-1",
        "Region": variables.get("Region"),
        "PrivateKey": "abc",
        "CaCert": """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA8QbLsBnQmXRFLONEkHL1LfvYZZi04HH5Kv4fX9UFT8S6vzwv
jrBu+oToMujfH+5O8eV4LTyovTuMnRZfFYmIRF0Y2EHFK05t5bu7PVE9gCFJitHS
Pj2YBVOYA8IfH0C6C9uE9pT35A/U54Apw2p36N8W8f3vYbCZH+4SlosfM68bWGAl
E7feqU6UHlo6+4IJdmwxH02siTTPoucaBgT4kBXcT5ylgozZl4tncLNHdsIYtXrk
VoCOcCF44uVin1H+hL8xtFM8+ovL7Eixr/KS+wtALlCODKzzQ3rBXgNixGHJUJKR
xBOPQZKULwqJAlvXfP6+QElK8vu0qySJ3FOhcQIDAQABAoIBAAPvZnfzk/JNcauv
8jihh9s+V2QhQCLB+Z14FK8N3U5WGe5xXx1nSAiTDu912d69l1BfvLyQVvjv9fXC
nb7ORglHs9YkDMIOP8EWdZIkt2pWIMtBbbtSah78JGk7TCLIfcEfzmXwPLPehk1Z
TFVCcb69lbRRvwzLQ1TAIFGQ5+uCEkW02KAl6kx+JnVpsE8/BjqZKG1Ne+sM6dOC
GRd44hgiNHKUT3Xtbw6jttiUFDLKYMYtb7PpRAkZFM8tgnBV6dWWJ3xTYW9kOjPh
XnScNARfphUZVibRhA04og5p1q/MUz9Sz9g2DURuSlo/MP3WZMbVRvZiUN1xhz5v
2WhsddkCgYEA+gWPFo0TbVbZXUrx9J/ptI9NXNx5zjyUrv87MDt1pnmMDgWrsCEI
RqQR4Lp2G11GA7IudiA/ipcZqgcRIIFvb+gu1kObox3BGGs59x+DqFeAPXt6dFG2
W10f9k96/tcbdursurqwd3Zv3cqQqRTKgaP4xHFmexlcwGCF5YwewWMCgYEA9sos
2acNINXwcNRUPnpg82DOrG9Zjr1aiNo9PDJmwGEdC9QMOUWM85dq0M9g388ttiLU
Wr/U4r5yDuqWJPcKtff2BaxSsZpcQ4Id9eddD9L+sxaBGyD23RtOC+IOlkG6WS4g
iUYulQvW69tBHWiwxQu7YMSIE2B3EuySPOQYlBsCgYEAxNwvqB/4lfT2PUDPdj+b
cnILBf0LY1nL8GZCol2O6z91CW1pm8rGi2iQMxRd/nnYsPxRHO2TWnpS2M+rqp5/
settRYQCPdMlwSZcg7oqnhgXf1GEP6Y/IX0Xt4cpXxLcKywarYRlggqdVlMyyA74
zE7hhzuK5442u7rEctN7O+UCgYAoM78ipafp1XAZsT0YAG+Stg504J7CNe5tpL+c
8sjyRd+pcZ2cJsxTUjNAWMf7LZDQvtPBBMb1OPjznRtgYi4IfqBBRFUkQXUOOkAP
MuViEokTO3NErBYK5svL+8NMjuCAbpc2RYyJEyiru0fcNpW1Q7f+h4VzQp+jIY6h
BLdMSQKBgGauU7OQksZCEY2MVAcD5dShYYvWLxOkj4dVVwISN1M6ImCAHwXZ6Nak
6YlzCGT+NbRJbB2cPfsrKXtAJVX15I3iDCKAoGkb+9kiHnPj7Q71KVuWQE6BQx7E
vE88TSsshwtX1s+qU9UWUrMPodK32q5nO3p8N033NvS9wLNfbcdc
-----END RSA PRIVATE KEY-----""",
    }
    try:
        resp = client.ulb().create_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["SSLId_01"] = utest.value_at_path(resp, "SSLId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateSSL",
)
def create_ssl_05(client, variables):
    d = {
        "UserCert": """-----BEGIN CERTIFICATE-----
MIIFzTCCBLWgAwIBAgIQQ8IswmAhEIKfNhrKqb0F3DANBgkqhkiG9w0BAQsFADCB
lzELMAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMs
IEluYy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsT
FERvbWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NM
IENBIC0gRzUwHhcNMTYxMjA2MDAwMDAwWhcNMTcxMjA2MjM1OTU5WjAgMR4wHAYD
VQQDDBVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQDxBsuwGdCZdEUs40SQcvUt+9hlmLTgcfkq/h9f1QVPxLq/PC+O
sG76hOgy6N8f7k7x5XgtPKi9O4ydFl8ViYhEXRjYQcUrTm3lu7s9UT2AIUmK0dI+
PZgFU5gDwh8fQLoL24T2lPfkD9TngCnDanfo3xbx/e9hsJkf7hKWix8zrxtYYCUT
t96pTpQeWjr7ggl2bDEfTayJNM+i5xoGBPiQFdxPnKWCjNmXi2dws0d2whi1euRW
gI5wIXji5WKfUf6EvzG0Uzz6i8vsSLGv8pL7C0AuUI4MrPNDesFeA2LEYclQkpHE
E49BkpQvCokCW9d8/r5ASUry+7SrJIncU6FxAgMBAAGjggKJMIIChTAgBgNVHREE
GTAXghVtLmVjb2xvZ3ktZW1vYmlsZS5jb20wCQYDVR0TBAIwADBhBgNVHSAEWjBY
MFYGBmeBDAECATBMMCMGCCsGAQUFBwIBFhdodHRwczovL2Quc3ltY2IuY29tL2Nw
czAlBggrBgEFBQcCAjAZDBdodHRwczovL2Quc3ltY2IuY29tL3JwYTAfBgNVHSME
GDAWgBRtWMd/GufhPy6mjJc1Qrv00zisPzAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0l
BBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMIGbBggrBgEFBQcBAQSBjjCBizA8Bggr
BgEFBQcwAYYwaHR0cDovL3RydXN0YXNpYTItb2NzcC5kaWdpdGFsY2VydHZhbGlk
YXRpb24uY29tMEsGCCsGAQUFBzAChj9odHRwOi8vdHJ1c3Rhc2lhMi1haWEuZGln
aXRhbGNlcnR2YWxpZGF0aW9uLmNvbS90cnVzdGFzaWFnNS5jcnQwggEDBgorBgEE
AdZ5AgQCBIH0BIHxAO8AdQDd6x0reg1PpiCLga2BaHB+Lo6dAdVciI09EcTNtuy+
zAAAAVjT7zdSAAAEAwBGMEQCIDCzWufc1q7hjmrrCetGyoA8EsEqpRSIhmZXStX5
8b7zAiA6x5aAaDK+yMyeAgw71yi3tRVrWayHN+W0+4BxC8u5UQB2AO5Lvbd1zmC6
4UJpH6vhnmajD35fsHLYgwDEe4l6qP3LAAABWNPvN4kAAAQDAEcwRQIgZ/LNgg7n
7AE4O2yZkrXNcqAOmJ3NU2nT6zcnBxPFTTsCIQCjyPbMfWMZTD3kxgxPQ1COw5zJ
sM0dfNmSr3MiU7EhqDANBgkqhkiG9w0BAQsFAAOCAQEAeyfgUhg9ZWVCaz0f+BQU
6fMMfmQ1BDzvVFu+ORoAqyJQogxwIdfjrlz/63YFee5qpUsW/aaz4ma3bb4dpE1K
GsgYe5N3o0xybYlOj+KB61sufYkzQS3HgDevCwjfUlGEbNl4dpO2xh5s5AANXlnz
s/X0+AJ33/bm+fWIjAbIjluaEoM6GETHTXi4Tlxy0j3nsXsB9tIIUibAdTtButef
JJRnikGRN+eHjrsLYe0RUmdKOQz1ik6teHt0MQX0aCe8OlXeyGDd9m8u7+y0nAnH
TVaNuT7vXMWyyXLVUcV898wkBo3Bo3hUiaw0QR0ttgDrf5ZwqPfqpytRW2K5GMZT
uw==
-----END CERTIFICATE-----


-----BEGIN CERTIFICATE-----
MIIFZTCCBE2gAwIBAgIQOhAOfxCeGsWcxf/2QNXkQjANBgkqhkiG9w0BAQsFADCB
yjELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL
ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNiBWZXJp
U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxW
ZXJpU2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0
aG9yaXR5IC0gRzUwHhcNMTYwODExMDAwMDAwWhcNMjYwODEwMjM1OTU5WjCBlzEL
MAkGA1UEBhMCQ04xJTAjBgNVBAoTHFRydXN0QXNpYSBUZWNobm9sb2dpZXMsIElu
Yy4xHzAdBgNVBAsTFlN5bWFudGVjIFRydXN0IE5ldHdvcmsxHTAbBgNVBAsTFERv
bWFpbiBWYWxpZGF0ZWQgU1NMMSEwHwYDVQQDExhUcnVzdEFzaWEgRFYgU1NMIENB
IC0gRzUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC39aSJZG/97x3a
6Qmuc9+MubagegRAVUmFYHTYTs8IKB2pM7wXN7W8mekdZaEgUjDFxvRBK/DhTb7U
8ONLsKKdT86aOhzbz2noCTn9wPWnGwkg+/4YKg/dPQQdV9tMsSu0cwqInWHxSAkm
AI1hYFC9D7Sf7Hp/5cRcD+dK454YMRzNOGLQnCVI8JEqrz6o9SOvQNTqTcfqt6DC
0UlXG+MPD1eNPjlzf1Vwaab+VSTgySoC+Ikbq2VsdykeOiGXW/OIiASH7+2LcR05
PmQ7GEOlM8yzoVojFpM8sHz+WxI05ZOPri5+vX3HhHHjWr5432G0dVmgohnZvlVZ
oy8XrlbpAgMBAAGjggF2MIIBcjASBgNVHRMBAf8ECDAGAQH/AgEAMC8GA1UdHwQo
MCYwJKAioCCGHmh0dHA6Ly9zLnN5bWNiLmNvbS9wY2EzLWc1LmNybDAOBgNVHQ8B
Af8EBAMCAQYwLgYIKwYBBQUHAQEEIjAgMB4GCCsGAQUFBzABhhJodHRwOi8vcy5z
eW1jZC5jb20wYQYDVR0gBFowWDBWBgZngQwBAgEwTDAjBggrBgEFBQcCARYXaHR0
cHM6Ly9kLnN5bWNiLmNvbS9jcHMwJQYIKwYBBQUHAgIwGRoXaHR0cHM6Ly9kLnN5
bWNiLmNvbS9ycGEwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMCkGA1Ud
EQQiMCCkHjAcMRowGAYDVQQDExFTeW1hbnRlY1BLSS0yLTYwMTAdBgNVHQ4EFgQU
bVjHfxrn4T8upoyXNUK79NM4rD8wHwYDVR0jBBgwFoAUf9Nlp8Ld7LvwMAnzQzn6
Aq8zMTMwDQYJKoZIhvcNAQELBQADggEBABUphhBbeG7scE3EveIN0dOjXPgwgQi8
I2ZAKYm6DawoGz1lEJVdvFmkyMbP973X80b7mKmn0nNbe1kjA4M0O0hHaMM1ZaEv
7e9vHEAoGyysMO6HzPWYMkyNxcCV7Nos2Uv4RvLDpQHh7P4Kt6fUU13ipcynrtQD
1lFUM0yoTzwwFsPu3Pk+94hL58ErqwqJQwxoHMgLIQeMVHeNKcWFy1bddSbIbCWU
Zs6cMxhrra062ZCpDCbxyEaFNGAtYQMqNz55Z/14XgSUONZ/cJTns6QKhpcgTOwB
fnNzRnk+aWreP7osKhXlz4zs+llP7goBDKFOMMtoEXx3YjJCKgpqmBU=
-----END CERTIFICATE-----""",
        "SSLName": "证书-2",
        "Region": variables.get("Region"),
        "PrivateKey": "abc",
        "CaCert": """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA8QbLsBnQmXRFLONEkHL1LfvYZZi04HH5Kv4fX9UFT8S6vzwv
jrBu+oToMujfH+5O8eV4LTyovTuMnRZfFYmIRF0Y2EHFK05t5bu7PVE9gCFJitHS
Pj2YBVOYA8IfH0C6C9uE9pT35A/U54Apw2p36N8W8f3vYbCZH+4SlosfM68bWGAl
E7feqU6UHlo6+4IJdmwxH02siTTPoucaBgT4kBXcT5ylgozZl4tncLNHdsIYtXrk
VoCOcCF44uVin1H+hL8xtFM8+ovL7Eixr/KS+wtALlCODKzzQ3rBXgNixGHJUJKR
xBOPQZKULwqJAlvXfP6+QElK8vu0qySJ3FOhcQIDAQABAoIBAAPvZnfzk/JNcauv
8jihh9s+V2QhQCLB+Z14FK8N3U5WGe5xXx1nSAiTDu912d69l1BfvLyQVvjv9fXC
nb7ORglHs9YkDMIOP8EWdZIkt2pWIMtBbbtSah78JGk7TCLIfcEfzmXwPLPehk1Z
TFVCcb69lbRRvwzLQ1TAIFGQ5+uCEkW02KAl6kx+JnVpsE8/BjqZKG1Ne+sM6dOC
GRd44hgiNHKUT3Xtbw6jttiUFDLKYMYtb7PpRAkZFM8tgnBV6dWWJ3xTYW9kOjPh
XnScNARfphUZVibRhA04og5p1q/MUz9Sz9g2DURuSlo/MP3WZMbVRvZiUN1xhz5v
2WhsddkCgYEA+gWPFo0TbVbZXUrx9J/ptI9NXNx5zjyUrv87MDt1pnmMDgWrsCEI
RqQR4Lp2G11GA7IudiA/ipcZqgcRIIFvb+gu1kObox3BGGs59x+DqFeAPXt6dFG2
W10f9k96/tcbdursurqwd3Zv3cqQqRTKgaP4xHFmexlcwGCF5YwewWMCgYEA9sos
2acNINXwcNRUPnpg82DOrG9Zjr1aiNo9PDJmwGEdC9QMOUWM85dq0M9g388ttiLU
Wr/U4r5yDuqWJPcKtff2BaxSsZpcQ4Id9eddD9L+sxaBGyD23RtOC+IOlkG6WS4g
iUYulQvW69tBHWiwxQu7YMSIE2B3EuySPOQYlBsCgYEAxNwvqB/4lfT2PUDPdj+b
cnILBf0LY1nL8GZCol2O6z91CW1pm8rGi2iQMxRd/nnYsPxRHO2TWnpS2M+rqp5/
settRYQCPdMlwSZcg7oqnhgXf1GEP6Y/IX0Xt4cpXxLcKywarYRlggqdVlMyyA74
zE7hhzuK5442u7rEctN7O+UCgYAoM78ipafp1XAZsT0YAG+Stg504J7CNe5tpL+c
8sjyRd+pcZ2cJsxTUjNAWMf7LZDQvtPBBMb1OPjznRtgYi4IfqBBRFUkQXUOOkAP
MuViEokTO3NErBYK5svL+8NMjuCAbpc2RYyJEyiru0fcNpW1Q7f+h4VzQp+jIY6h
BLdMSQKBgGauU7OQksZCEY2MVAcD5dShYYvWLxOkj4dVVwISN1M6ImCAHwXZ6Nak
6YlzCGT+NbRJbB2cPfsrKXtAJVX15I3iDCKAoGkb+9kiHnPj7Q71KVuWQE6BQx7E
vE88TSsshwtX1s+qU9UWUrMPodK32q5nO3p8N033NvS9wLNfbcdc
-----END RSA PRIVATE KEY-----""",
    }
    try:
        resp = client.ulb().create_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["SSLId_02"] = utest.value_at_path(resp, "SSLId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.SSLId", variables.get("SSLId_01")),
    ],
    action="DescribeSSL",
)
def describe_ssl_06(client, variables):
    d = {"SSLId": variables.get("SSLId_01"), "Region": variables.get("Region")}
    try:
        resp = client.ulb().describe_ssl(d)
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
        ("str_eq", "DataSet.0.SSLId", variables.get("SSLId_02")),
    ],
    action="DescribeSSL",
)
def describe_ssl_07(client, variables):
    d = {"SSLId": variables.get("SSLId_02"), "Region": variables.get("Region")}
    try:
        resp = client.ulb().describe_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="BindSSL",
)
def bind_ssl_08(client, variables):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "SSLId": variables.get("SSLId_01"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.ulb().bind_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="UpdateSSLBinding",
)
def update_ssl_binding_09(client, variables):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
        "OldSSLId": variables.get("SSLId_01"),
        "NewSSLId": variables.get("SSLId_02"),
    }
    try:
        resp = client.invoke("UpdateSSLBinding", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="UnbindSSL",
)
def unbind_ssl_10(client, variables):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "SSLId": variables.get("SSLId_02"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.ulb().unbind_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSSL",
)
def delete_ssl_11(client, variables):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "SSLId": variables.get("SSLId_01"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.ulb().delete_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSSL",
)
def delete_ssl_12(client, variables):
    d = {"SSLId": variables.get("SSLId_02"), "Region": variables.get("Region")}
    try:
        resp = client.ulb().delete_ssl(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteVServer",
)
def delete_vserver_13(client, variables):
    d = {
        "VServerId": variables.get("VServerId"),
        "ULBId": variables.get("ULBId"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.ulb().delete_vserver(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteULB",
)
def delete_ulb_14(client, variables):
    d = {"ULBId": variables.get("ULBId"), "Region": variables.get("Region")}
    try:
        resp = client.ulb().delete_ulb(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=5,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteSubnet",
)
def delete_subnet_15(client, variables):
    d = {
        "SubnetId": variables.get("subnet_id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.vpc().delete_subnet(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DeleteVPC",
)
def delete_vpc_16(client, variables):
    d = {"VPCId": variables.get("vpc_id"), "Region": variables.get("Region")}
    try:
        resp = client.vpc().delete_vpc(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp