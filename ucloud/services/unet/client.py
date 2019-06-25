# -*- coding: utf-8 -*-

from ucloud.core.client import Client
from ucloud.services.unet.schemas import apis


class UNetClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(UNetClient, self).__init__(config, transport, middleware, logger)

    def allocate_e_ip(self, req=None, **kwargs):
        """ AllocateEIP - 根据提供信息, 申请弹性IP

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        - **Region** (str) - (Config) 地域。
        - **Bandwidth** (int) - (Required) 弹性IP的外网带宽, 单位为Mbps. 共享带宽模式必须指定0M带宽, 非共享带宽模式必须指定非0Mbps带宽. 各地域非共享带宽的带宽范围如下： 流量计费[1-200]，带宽计费[1-800]
        - **OperatorName** (str) - (Required) 弹性IP的线路如下: 国际: International BGP: Bgp  各地域允许的线路参数如下:  cn-sh1: Bgp cn-sh2: Bgp cn-gd: Bgp cn-bj1: Bgp cn-bj2: Bgp hk: International us-ca: International th-bkk: International  kr-seoul:International  us-ws:International  ge-fra:International  sg:International  tw-kh:International.其他海外线路均为 International
        - **ChargeType** (str) - 付费方式, 枚举值为: Year, 按年付费; Month, 按月付费; Dynamic, 按需付费(需开启权限); Trial, 试用(需开启权限) 默认为按月付费
        - **CouponId** (str) - 代金券ID, 默认不使用
        - **Name** (str) - 弹性IP的名称, 默认为 "EIP"
        - **PayMode** (str) - 弹性IP的计费模式. 枚举值: "Traffic", 流量计费; "Bandwidth", 带宽计费; "ShareBandwidth",共享带宽模式. 默认为 "Bandwidth".
        - **Quantity** (int) - 购买时长, 默认: 1
        - **Remark** (str) - 弹性IP的备注, 默认为空
        - **ShareBandwidthId** (str) - 绑定的共享带宽Id，仅当PayMode为ShareBandwidth时有效
        - **Tag** (str) - 业务组名称, 默认为 "Default"
        
        **Response**

        - **EIPSet** (list) - 见 **UnetAllocateEIPSet** 模型定义
        
        **Response Model**
        
        **UnetEIPAddrSet** 
        
        - **OperatorName** (str) - 运营商信息如: 电信: Telecom, 联通: Unicom, 国际: International, Duplet: 双线IP（电信+联通), BGP: Bgp
        - **IP** (str) - IP地址

        **UnetAllocateEIPSet** 
        
        - **EIPId** (str) - 申请到的EIP资源ID
        - **EIPAddr** (list) - 见 **UnetEIPAddrSet** 模型定义

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateEIPRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("AllocateEIP", d, **kwargs)
        return apis.AllocateEIPResponseSchema().loads(resp)

    def allocate_share_bandwidth(self, req=None, **kwargs):
        """ AllocateShareBandwidth - 开通共享带宽

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - (Required) 付费方式:Year 按年,Month 按月,Dynamic 按时;
        - **Name** (str) - (Required) 共享带宽名字
        - **ShareBandwidth** (int) - (Required) 共享带宽值
        - **Quantity** (int) - 购买时长
        - **ShareBandwidthGuarantee** (int) - 共享带宽保底值(后付费)
        
        **Response**

        - **ShareBandwidthId** (str) - 共享带宽资源Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateShareBandwidthRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("AllocateShareBandwidth", d, **kwargs)
        return apis.AllocateShareBandwidthResponseSchema().loads(resp)

    def allocate_v_ip(self, req=None, **kwargs):
        """ AllocateVIP - 根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域
        - **SubnetId** (str) - (Required) 子网id
        - **VPCId** (str) - (Required) 指定vip所属的VPC
        - **BusinessId** (str) - 业务组
        - **Count** (int) - 申请数量，默认: 1
        - **Name** (str) - vip名，默认为VIP
        - **Remark** (str) - 备注
        - **Tag** (str) - 业务组名称，默认为Default
        - **Zone** (str) - 可用区
        
        **Response**

        - **DataSet** (list) - 申请到的VIP地址
        - **VIPSet** (list) - 见 **VIPSet** 模型定义
        
        **Response Model**
        
        **VIPSet** 
        
        - **VIP** (str) - 虚拟ip
        - **VIPId** (str) - 虚拟ip id
        - **VPCId** (str) - VPC id

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateVIPRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("AllocateVIP", d, **kwargs)
        return apis.AllocateVIPResponseSchema().loads(resp)

    def associate_e_ip_with_share_bandwidth(self, req=None, **kwargs):
        """ AssociateEIPWithShareBandwidth - 将EIP加入共享带宽

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        - **Region** (str) - (Config) 地域。
        - **EIPIds** (list) - (Required) 要加入共享带宽的EIP的资源Id
        - **ShareBandwidthId** (str) - (Required) 共享带宽ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AssociateEIPWithShareBandwidthRequestSchema().dumps(d)
        resp = self.invoke("AssociateEIPWithShareBandwidth", d, **kwargs)
        return apis.AssociateEIPWithShareBandwidthResponseSchema().loads(resp)

    def bind_e_ip(self, req=None, **kwargs):
        """ BindEIP - 将尚未使用的弹性IP绑定到指定的资源

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **EIPId** (str) - (Required) 弹性IP的资源Id
        - **ResourceId** (str) - (Required) 弹性IP请求绑定的资源ID
        - **ResourceType** (str) - (Required) 弹性IP请求绑定的资源类型, 枚举值为: uhost: 云主机; ulb, 负载均衡器 upm: 物理机; hadoophost: 大数据集群;fortresshost：堡垒机；udockhost：容器；udhost：私有专区主机；natgw：natgw；udb：udb；vpngw：ipsec vpn；ucdr：云灾备；dbaudit：数据库审计；uni：虚拟网卡。
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BindEIPRequestSchema().dumps(d)
        resp = self.invoke("BindEIP", d, **kwargs)
        return apis.BindEIPResponseSchema().loads(resp)

    def create_bandwidth_package(self, req=None, **kwargs):
        """ CreateBandwidthPackage - 为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。
        - **Region** (str) - (Config) 地域
        - **Bandwidth** (int) - (Required) 带宽大小(单位Mbps), 取值范围[2,800] (最大值受地域限制)
        - **EIPId** (str) - (Required) 所绑定弹性IP的资源ID
        - **TimeRange** (int) - (Required) 带宽包有效时长, 取值范围为大于0的整数, 即该带宽包在EnableTime到 EnableTime+TimeRange时间段内生效
        - **CouponId** (str) - 代金券ID
        - **EnableTime** (int) - 生效时间, 格式为 Unix timestamp, 默认为立即开通
        
        **Response**

        - **BandwidthPackageId** (str) - 所创建带宽包的资源ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateBandwidthPackageRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateBandwidthPackage", d, **kwargs)
        return apis.CreateBandwidthPackageResponseSchema().loads(resp)

    def create_firewall(self, req=None, **kwargs):
        """ CreateFirewall - 创建防火墙

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **Name** (str) - (Required) 防火墙名称
        - **Rule** (list) - (Required) 防火墙规则，例如：TCP|22|192.168.1.1/22|DROP|LOW|禁用22端口，第一个参数代表协议：第二个参数代表端口号，第三个参数为ip，第四个参数为ACCEPT（接受）和DROP（拒绝），第五个参数优先级：HIGH（高），MEDIUM（中），LOW（低），第六个参数为该条规则的自定义备注
        - **Remark** (str) - 防火墙描述，默认为空
        - **Tag** (str) - 防火墙业务组，默认为Default
        
        **Response**

        - **FWId** (str) - 防火墙ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateFirewallRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateFirewall", d, **kwargs)
        return apis.CreateFirewallResponseSchema().loads(resp)

    def delete_bandwidth_package(self, req=None, **kwargs):
        """ DeleteBandwidthPackage - 删除弹性IP上已附加带宽包

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **BandwidthPackageId** (str) - (Required) 带宽包资源ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteBandwidthPackageRequestSchema().dumps(d)
        resp = self.invoke("DeleteBandwidthPackage", d, **kwargs)
        return apis.DeleteBandwidthPackageResponseSchema().loads(resp)

    def delete_firewall(self, req=None, **kwargs):
        """ DeleteFirewall - 删除防火墙

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **FWId** (str) - (Required) 防火墙资源ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteFirewallRequestSchema().dumps(d)
        resp = self.invoke("DeleteFirewall", d, **kwargs)
        return apis.DeleteFirewallResponseSchema().loads(resp)

    def describe_bandwidth_package(self, req=None, **kwargs):
        """ DescribeBandwidthPackage - 获取某地域下的带宽包信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - 返回数据分页值, 取值范围为 [0,10000000] 之间的整数, 默认为20
        - **Offset** (int) - 返回数据偏移量, 默认为0
        
        **Response**

        - **DataSets** (list) - 见 **UnetBandwidthPackageSet** 模型定义
        - **TotalCount** (int) - 满足条件的带宽包总数
        
        **Response Model**
        
        **EIPAddrSet** 
        
        - **OperatorName** (str) - 运营商信息, 枚举值为: Telecom 电信; Unicom: 联通; Duplet: 双线; Bgp: BGP; International: 国际.
        - **IP** (str) - 弹性IP地址

        **UnetBandwidthPackageSet** 
        
        - **Bandwidth** (int) - 带宽包的临时带宽值, 单位Mbps
        - **EIPId** (str) - 带宽包所绑定弹性IP的资源ID
        - **EIPAddr** (list) - 见 **EIPAddrSet** 模型定义
        - **BandwidthPackageId** (str) - 带宽包的资源ID
        - **EnableTime** (int) - 生效时间, 格式为 Unix Timestamp
        - **DisableTime** (int) - 失效时间, 格式为 Unix Timestamp
        - **CreateTime** (int) - 创建时间, 格式为 Unix Timestamp

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeBandwidthPackageRequestSchema().dumps(d)
        resp = self.invoke("DescribeBandwidthPackage", d, **kwargs)
        return apis.DescribeBandwidthPackageResponseSchema().loads(resp)

    def describe_bandwidth_usage(self, req=None, **kwargs):
        """ DescribeBandwidthUsage - 获取带宽用量信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **EIPIds** (list) - 弹性IP的资源Id. 如果为空, 则返回当前 Region中符合条件的所有EIP的带宽用量, n为自然数
        - **Limit** (int) - 返回数据分页值, 取值范围为 [0,10000000] 之间的整数, 默认为20
        - **OffSet** (int) - 返回数据偏移量, 默认为0
        
        **Response**

        - **TotalCount** (int) - EIPSet中的元素个数
        - **EIPSet** (list) - 见 **UnetBandwidthUsageEIPSet** 模型定义
        
        **Response Model**
        
        **UnetBandwidthUsageEIPSet** 
        
        - **CurBandwidth** (float) - 最近5分钟带宽用量, 单位Mbps
        - **EIPId** (str) - 弹性IP资源ID

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeBandwidthUsageRequestSchema().dumps(d)
        resp = self.invoke("DescribeBandwidthUsage", d, **kwargs)
        return apis.DescribeBandwidthUsageResponseSchema().loads(resp)

    def describe_e_ip(self, req=None, **kwargs):
        """ DescribeEIP - 获取弹性IP信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **EIPIds** (list) - 弹性IP的资源ID如果为空, 则返回当前 Region中符合条件的的所有EIP
        - **Limit** (int) - 数据分页值, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0
        
        **Response**

        - **TotalCount** (int) - 满足条件的弹性IP总数
        - **TotalBandwidth** (int) - 满足条件的弹性IP带宽总和, 单位Mbps
        - **EIPSet** (list) - 见 **UnetEIPSet** 模型定义
        
        **Response Model**
        
        **UnetEIPAddrSet** 
        
        - **OperatorName** (str) - 运营商信息如: 电信: Telecom, 联通: Unicom, 国际: International, Duplet: 双线IP（电信+联通), BGP: Bgp
        - **IP** (str) - IP地址

        **UnetEIPResourceSet** 
        
        - **ResourceType** (str) - 已绑定的资源类型, 枚举值为: uhost, 云主机；natgw：NAT网关；ulb：负载均衡器；upm: 物理机; hadoophost: 大数据集群;fortresshost：堡垒机；udockhost：容器；udhost：私有专区主机；vpngw：IPSec VPN；ucdr：云灾备；dbaudit：数据库审计，uni：虚拟网卡。
        - **ResourceName** (str) - 已绑定的资源名称
        - **ResourceId** (str) - 已绑定资源的资源ID
        - **SubResourceType** (str) - 资源绑定的虚拟网卡的类型。uni，虚拟网卡。
        - **SubResourceName** (str) - 资源绑定的虚拟网卡的名称
        - **SubResourceId** (str) - 资源绑定的虚拟网卡的ID
        - **EIPId** (str) - 弹性IP的资源ID

        **ShareBandwidthSet** 
        
        - **ShareBandwidthName** (str) - 共享带宽的资源名称
        - **ShareBandwidthId** (str) - 共享带宽ID
        - **ShareBandwidth** (int) - 共享带宽带宽值

        **UnetEIPSet** 
        
        - **Remark** (str) - 弹性IP的备注, 缺省值为 ""
        - **PayMode** (str) - 弹性IP的计费模式, 枚举值为: "Bandwidth", 带宽计费; "Traffic", 流量计费; "ShareBandwidth",共享带宽模式. 默认为 "Bandwidth".
        - **Expire** (bool) - 弹性IP是否到期
        - **EIPId** (str) - 弹性IP的资源ID
        - **Status** (str) - 弹性IP的资源绑定状态, 枚举值为: used: 已绑定, free: 未绑定, freeze: 已冻结
        - **Name** (str) - 弹性IP的名称,缺省值为 "EIP"
        - **ShareBandwidthSet** (dict) - 见 **ShareBandwidthSet** 模型定义
        - **Tag** (str) - 弹性IP的业务组标识, 缺省值为 "Default"
        - **Weight** (int) - 外网出口权重, 默认为50, 范围[0-100]
        - **ChargeType** (str) - 付费方式, 枚举值为: Year, 按年付费; Month, 按月付费; Dynamic, 按小时付费; Trial, 试用. 按小时付费和试用这两种付费模式需要开通权限.
        - **CreateTime** (int) - 弹性IP的创建时间, 格式为Unix Timestamp
        - **Resource** (dict) - 见 **UnetEIPResourceSet** 模型定义
        - **EIPAddr** (list) - 见 **UnetEIPAddrSet** 模型定义
        - **BandwidthType** (int) - 带宽模式, 枚举值为: 0: 非共享带宽模式, 1: 共享带宽模式
        - **Bandwidth** (int) - 弹性IP的带宽, 单位为Mbps, 当BandwidthType=1时, 该处显示为共享带宽值. 当BandwidthType=0时, 该处显示这个弹性IP的带宽.
        - **ExpireTime** (int) - 弹性IP的到期时间, 格式为Unix Timestamp

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeEIPRequestSchema().dumps(d)
        resp = self.invoke("DescribeEIP", d, **kwargs)
        return apis.DescribeEIPResponseSchema().loads(resp)

    def describe_firewall(self, req=None, **kwargs):
        """ DescribeFirewall - 获取防火墙组信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **FWId** (str) - 防火墙ID，默认为返回所有防火墙
        - **Limit** (int) - 返回数据长度，默认为20，最大10000000
        - **Offset** (int) - 列表起始位置偏移量，默认为0
        - **ResourceId** (str) - 绑定防火墙组的资源ID
        - **ResourceType** (str) - 绑定防火墙组的资源类型，默认为全部资源类型。枚举值为："unatgw"，NAT网关； "uhost"，云主机； "upm"，物理云主机； "hadoophost"，hadoop节点； "fortresshost"，堡垒机； "udhost"，私有专区主机；"udockhost"，容器；"dbaudit"，数据库审计.
        
        **Response**

        - **TotalCount** (int) - 
        - **DataSet** (list) - 见 **FirewallDataSet** 模型定义
        
        **Response Model**
        
        **FirewallRuleSet** 
        
        - **RuleAction** (str) - 防火墙动作
        - **Remark** (str) - 防火墙规则备注
        - **SrcIP** (str) - 源地址
        - **Priority** (str) - 优先级
        - **ProtocolType** (str) - 协议类型
        - **DstPort** (str) - 目标端口

        **FirewallDataSet** 
        
        - **GroupId** (str) - 安全组ID（即将废弃）
        - **Tag** (str) - 防火墙业务组
        - **Type** (str) - 防火墙组类型，枚举值为： "user defined", 用户自定义防火墙； "recommend web", 默认Web防火墙； "recommend non web", 默认非Web防火墙
        - **Rule** (list) - 见 **FirewallRuleSet** 模型定义
        - **FWId** (str) - 防火墙ID
        - **Name** (str) - 防火墙名称
        - **Remark** (str) - 防火墙备注
        - **ResourceCount** (int) - 防火墙绑定资源数量
        - **CreateTime** (int) - 防火墙组创建时间，格式为Unix Timestamp

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeFirewallRequestSchema().dumps(d)
        resp = self.invoke("DescribeFirewall", d, **kwargs)
        return apis.DescribeFirewallResponseSchema().loads(resp)

    def describe_firewall_resource(self, req=None, **kwargs):
        """ DescribeFirewallResource - 获取防火墙组所绑定资源的外网IP

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **FWId** (str) - (Required) 防火墙ID
        - **Limit** (int) - 返回数据长度，默认为20，最大10000000
        - **Offset** (int) - 列表起始位置偏移量，默认为0
        
        **Response**

        - **ResourceSet** (list) - 见 **ResourceSet** 模型定义
        - **TotalCount** (int) - 绑定资源总数
        
        **Response Model**
        
        **ResourceSet** 
        
        - **Status** (int) - 状态
        - **Tag** (str) - 业务组
        - **Zone** (int) - 可用区
        - **Name** (str) - 名称
        - **PrivateIP** (str) - 内网IP
        - **Remark** (str) - 备注
        - **ResourceID** (str) - 绑定该防火墙的资源id
        - **ResourceType** (str) - 绑定资源的资源类型，如"uhost","upm","umem","uhive","uvip","uredis","uhadoop","ufortress","dbaudit","udw","udocker", "umemcache"

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeFirewallResourceRequestSchema().dumps(d)
        resp = self.invoke("DescribeFirewallResource", d, **kwargs)
        return apis.DescribeFirewallResourceResponseSchema().loads(resp)

    def describe_share_bandwidth(self, req=None, **kwargs):
        """ DescribeShareBandwidth - 获取共享带宽信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ShareBandwidthIds** (list) - 需要返回的共享带宽Id
        
        **Response**

        - **DataSet** (list) - 见 **UnetShareBandwidthSet** 模型定义
        - **TotalCount** (int) - 符合条件的共享带宽总数，大于等于返回DataSet长度
        
        **Response Model**
        
        **EIPAddrSet** 
        
        - **OperatorName** (str) - 运营商信息, 枚举值为: Telecom 电信; Unicom: 联通; Duplet: 双线; Bgp: BGP; International: 国际.
        - **IP** (str) - 弹性IP地址

        **EIPSetData** 
        
        - **Bandwidth** (int) - EIP带宽值
        - **EIPAddr** (list) - 见 **EIPAddrSet** 模型定义
        - **EIPId** (str) - EIP资源Id

        **UnetShareBandwidthSet** 
        
        - **EIPSet** (list) - 见 **EIPSetData** 模型定义
        - **Name** (str) - 共享带宽名称
        - **ShareBandwidth** (int) - 共享带宽值(预付费)/共享带宽峰值(后付费), 单位Mbps
        - **CreateTime** (int) - 创建时间, 格式为Unix Timestamp
        - **ExpireTime** (int) - 过期时间, 格式为Unix Timestamp
        - **PostPayStartTime** (int) - 共享带宽后付费开始计费时间(后付费)
        - **ShareBandwidthId** (str) - 共享带宽的资源ID
        - **ChargeType** (str) - 付费方式, 预付费:Year 按年,Month 按月,Dynamic 按需;后付费:PostPay(按月)
        - **BandwidthGuarantee** (int) - 共享带宽保底值(后付费)

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeShareBandwidthRequestSchema().dumps(d)
        resp = self.invoke("DescribeShareBandwidth", d, **kwargs)
        return apis.DescribeShareBandwidthResponseSchema().loads(resp)

    def describe_v_ip(self, req=None, **kwargs):
        """ DescribeVIP - 获取内网VIP详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BusinessId** (str) - 业务组
        - **SubnetId** (str) - 子网id，不指定则获取VPCId下的所有vip
        - **Tag** (str) - 业务组名称, 默认为 Default
        - **VPCId** (str) - vpc的id,指定SubnetId时必填
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **VIPSet** (list) - 见 **VIPDetailSet** 模型定义
        - **DataSet** (list) - 内网VIP地址列表
        - **TotalCount** (int) - vip数量
        
        **Response Model**
        
        **VIPDetailSet** 
        
        - **RealIp** (str) - 真实主机ip
        - **VIP** (str) - 虚拟ip
        - **SubnetId** (str) - 子网id
        - **VPCId** (str) - VPC id
        - **Name** (str) - 
        - **Zone** (str) - 地域
        - **VIPId** (str) - 虚拟ip id
        - **CreateTime** (int) - 创建时间

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVIPRequestSchema().dumps(d)
        resp = self.invoke("DescribeVIP", d, **kwargs)
        return apis.DescribeVIPResponseSchema().loads(resp)

    def disassociate_e_ip_with_share_bandwidth(self, req=None, **kwargs):
        """ DisassociateEIPWithShareBandwidth - 将EIP移出共享带宽

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 移出共享带宽后，EIP的外网带宽, 单位为Mbps. 各地域带宽范围如下：  流量计费[1-200],带宽计费[1-800]
        - **ShareBandwidthId** (str) - (Required) 共享带宽ID
        - **EIPIds** (list) - EIP的资源Id；默认移出该共享带宽下所有的EIP
        - **PayMode** (str) - 移出共享带宽后，EIP的计费模式. 枚举值: "Traffic", 流量计费; "Bandwidth", 带宽计费;  默认为 "Bandwidth".
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DisassociateEIPWithShareBandwidthRequestSchema().dumps(d)
        resp = self.invoke("DisassociateEIPWithShareBandwidth", d, **kwargs)
        return apis.DisassociateEIPWithShareBandwidthResponseSchema().loads(resp)

    def get_e_ip_pay_mode(self, req=None, **kwargs):
        """ GetEIPPayMode - 获取弹性IP计费模式

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **EIPId** (list) - (Required) 弹性IP的资源Id
        
        **Response**

        - **EIPPayMode** (list) - 见 **EIPPayModeSet** 模型定义
        
        **Response Model**
        
        **EIPPayModeSet** 
        
        - **EIPPayMode** (str) - EIP的计费模式. 枚举值为：Bandwidth, 带宽计费;Traffic, 流量计费; "ShareBandwidth",共享带宽模式
        - **EIPId** (str) - EIP的资源ID

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetEIPPayModeRequestSchema().dumps(d)
        resp = self.invoke("GetEIPPayMode", d, **kwargs)
        return apis.GetEIPPayModeResponseSchema().loads(resp)

    def get_e_ip_price(self, req=None, **kwargs):
        """ GetEIPPrice - 获取弹性IP价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 弹性IP的外网带宽, 单位为Mbps, 范围 [0-800]
        - **OperatorName** (str) - (Required) 弹性IP的线路如下: 国际: International BGP: Bgp 各地域允许的线路参数如下: cn-sh1: Bgp cn-sh2: Bgp cn-gd: Bgp cn-bj1: Bgp cn-bj2: Bgp hk: International us-ca: International th-bkk: International kr-seoul:International us-ws:International ge-fra:International sg:International tw-kh:International.其他海外线路均为 International,泉州为移动单线cn-qz:ChinaMobile
        - **ChargeType** (str) - 付费方式, 枚举值为: Year, 按年付费; Month, 按月付费; Dynamic, 按时付费; 默认为获取三种价格
        - **PayMode** (str) - 弹性IP计费方式r. 枚举值为: Traffic, 流量计费; Bandwidth, 带宽计费; "ShareBandwidth",共享带宽模式. 默认为Bandwidth
        - **Quantity** (int) - 购买时长。默认: 1。按小时购买(Dynamic)时无需此参数。 月付时，此参数传0，代表了购买至月末
        
        **Response**

        - **PriceSet** (list) - 见 **EIPPriceDetailSet** 模型定义
        
        **Response Model**
        
        **EIPPriceDetailSet** 
        
        - **PurchaseValue** (int) - 资源有效期, 以Unix Timestamp表示
        - **ChargeType** (str) - 弹性IP付费方式
        - **Price** (float) - 弹性IP价格, 单位"元"

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetEIPPriceRequestSchema().dumps(d)
        resp = self.invoke("GetEIPPrice", d, **kwargs)
        return apis.GetEIPPriceResponseSchema().loads(resp)

    def get_e_ip_upgrade_price(self, req=None, **kwargs):
        """ GetEIPUpgradePrice - 获取弹性IP带宽改动价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 弹性IP的外网带宽, 单位为Mbps, 范围 [1-800]
        - **EIPId** (str) - (Required) 弹性IP的资源ID
        
        **Response**

        - **Price** (float) - 调整带宽后的EIP价格, 单位为"元", 如需退费此处为负值
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetEIPUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("GetEIPUpgradePrice", d, **kwargs)
        return apis.GetEIPUpgradePriceResponseSchema().loads(resp)

    def grant_firewall(self, req=None, **kwargs):
        """ GrantFirewall - 将防火墙应用到资源上

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **FWId** (str) - (Required) 防火墙资源ID
        - **ResourceId** (str) - (Required) 所应用资源ID
        - **ResourceType** (str) - (Required) 绑定防火墙组的资源类型，默认为全部资源类型。枚举值为："unatgw"，NAT网关； "uhost"，云主机； "upm"，物理云主机； "hadoophost"，hadoop节点； "fortresshost"，堡垒机； "udhost"，私有专区主机；"udockhost"，容器；"dbaudit"，数据库审计，”uni“，虚拟网卡。
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GrantFirewallRequestSchema().dumps(d)
        resp = self.invoke("GrantFirewall", d, **kwargs)
        return apis.GrantFirewallResponseSchema().loads(resp)

    def modify_e_ip_bandwidth(self, req=None, **kwargs):
        """ ModifyEIPBandwidth - 调整弹性IP的外网带宽

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 弹性IP的外网带宽, 单位为Mbps. 各地域的带宽值范围如下：流量计费[1-200],带宽计费[1-800]
        - **EIPId** (str) - (Required) 弹性IP的资源ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyEIPBandwidthRequestSchema().dumps(d)
        resp = self.invoke("ModifyEIPBandwidth", d, **kwargs)
        return apis.ModifyEIPBandwidthResponseSchema().loads(resp)

    def modify_e_ip_weight(self, req=None, **kwargs):
        """ ModifyEIPWeight - 修改弹性IP的外网出口权重

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **EIPId** (str) - (Required) 弹性IP的资源ID
        - **Weight** (int) - (Required) 外网出口权重, 范围[0-100] 取值为0时, 该弹性IP不会被使用. 取值为100时, 同主机下只会使用这个弹性IP，其他弹性IP不会被使用 请勿将多个绑定在同一资源的弹性IP设置为相同权重
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyEIPWeightRequestSchema().dumps(d)
        resp = self.invoke("ModifyEIPWeight", d, **kwargs)
        return apis.ModifyEIPWeightResponseSchema().loads(resp)

    def release_e_ip(self, req=None, **kwargs):
        """ ReleaseEIP - 释放弹性IP资源, 所释放弹性IP必须为非绑定状态.

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **EIPId** (str) - (Required) 弹性IP的资源ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseEIPRequestSchema().dumps(d)
        resp = self.invoke("ReleaseEIP", d, **kwargs)
        return apis.ReleaseEIPResponseSchema().loads(resp)

    def release_share_bandwidth(self, req=None, **kwargs):
        """ ReleaseShareBandwidth - 关闭共享带宽

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **EIPBandwidth** (int) - (Required) 关闭共享带宽后，各EIP恢复为的带宽值
        - **ShareBandwidthId** (str) - (Required) 共享带宽ID
        - **PayMode** (str) - Bandwidth 带宽计费, Traffic 转流量计费
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseShareBandwidthRequestSchema().dumps(d)
        resp = self.invoke("ReleaseShareBandwidth", d, **kwargs)
        return apis.ReleaseShareBandwidthResponseSchema().loads(resp)

    def release_v_ip(self, req=None, **kwargs):
        """ ReleaseVIP - 释放VIP资源

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写
        - **Region** (str) - (Config) 地域
        - **VIPId** (str) - (Required) 内网VIP的id
        - **Zone** (str) - 可用区
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseVIPRequestSchema().dumps(d)
        resp = self.invoke("ReleaseVIP", d, **kwargs)
        return apis.ReleaseVIPResponseSchema().loads(resp)

    def resize_share_bandwidth(self, req=None, **kwargs):
        """ ResizeShareBandwidth - 调整共享带宽的带宽值

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ShareBandwidth** (int) - (Required) 带宽值，单位为Mb，范围 [20-5000] (最大值受地域限制)
        - **ShareBandwidthId** (str) - (Required) 共享带宽的Id
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeShareBandwidthRequestSchema().dumps(d)
        resp = self.invoke("ResizeShareBandwidth", d, **kwargs)
        return apis.ResizeShareBandwidthResponseSchema().loads(resp)

    def set_e_ip_pay_mode(self, req=None, **kwargs):
        """ SetEIPPayMode - 设置弹性IP计费模式, 切换时会涉及付费/退费.

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 调整的目标带宽值, 单位Mbps. 各地域的带宽值范围如下: 流量计费[1-200],其余情况[1-800]
        - **EIPId** (str) - (Required) 弹性IP的资源Id
        - **PayMode** (str) - (Required) 计费模式. 枚举值："Traffic", 流量计费模式; "Bandwidth", 带宽计费模式
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.SetEIPPayModeRequestSchema().dumps(d)
        resp = self.invoke("SetEIPPayMode", d, **kwargs)
        return apis.SetEIPPayModeResponseSchema().loads(resp)

    def un_bind_e_ip(self, req=None, **kwargs):
        """ UnBindEIP - 将弹性IP从资源上解绑

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **EIPId** (str) - (Required) 弹性IP的资源Id
        - **ResourceId** (str) - (Required) 弹性IP请求解绑的资源ID
        - **ResourceType** (str) - (Required) 弹性IP请求解绑的资源类型, 枚举值为: uhost: 云主机; ulb, 负载均衡器 upm: 物理机; hadoophost: 大数据集群;fortresshost：堡垒机；udockhost：容器；udhost：私有专区主机；natgw：NAT网关；udb：udb；vpngw：ipsec vpn；ucdr：云灾备；dbaudit：数据库审计；uni，虚拟网卡。
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UnBindEIPRequestSchema().dumps(d)
        resp = self.invoke("UnBindEIP", d, **kwargs)
        return apis.UnBindEIPResponseSchema().loads(resp)

    def update_e_ip_attribute(self, req=None, **kwargs):
        """ UpdateEIPAttribute - 更新弹性IP名称，业务组，备注等属性字段

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **EIPId** (str) - (Required) EIP资源ID
        - **Name** (str) - 名字（Name Tag Remark都为空则报错）
        - **Remark** (str) - 备注
        - **Tag** (str) - 业务
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateEIPAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateEIPAttribute", d, **kwargs)
        return apis.UpdateEIPAttributeResponseSchema().loads(resp)

    def update_firewall(self, req=None, **kwargs):
        """ UpdateFirewall - 更新防火墙规则

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **FWId** (str) - (Required) 防火墙资源ID
        - **Rule** (list) - (Required) 防火墙规则，例如：TCP|22|192.168.1.1/22|DROP|LOW|禁用22端口，第一个参数代表协议：第二个参数代表端口号，第三个参数为ip，第四个参数为ACCEPT（接受）和DROP（拒绝），第五个参数优先级：HIGH（高），MEDIUM（中），LOW（低），第六个参数为该条规则的自定义备注
        
        **Response**

        - **FWId** (str) - 防火墙id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateFirewallRequestSchema().dumps(d)
        resp = self.invoke("UpdateFirewall", d, **kwargs)
        return apis.UpdateFirewallResponseSchema().loads(resp)

    def update_firewall_attribute(self, req=None, **kwargs):
        """ UpdateFirewallAttribute - 更新防火墙规则

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **FWId** (str) - (Required) 防火墙资源ID
        - **Name** (str) - 防火墙名称，默认为空，为空则不做修改。Name,Tag,Remark必须填写1个及以上
        - **Remark** (str) - 防火墙备注，默认为空，为空则不做修改。Name,Tag,Remark必须填写1个及以上
        - **Tag** (str) - 防火墙业务组，默认为空，为空则不做修改。Name,Tag,Remark必须填写1个及以上
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateFirewallAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateFirewallAttribute", d, **kwargs)
        return apis.UpdateFirewallAttributeResponseSchema().loads(resp)
