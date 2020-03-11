# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
from ucloud.core.client import Client
from ucloud.services.vpc.schemas import apis


class VPCClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(VPCClient, self).__init__(config, transport, middleware, logger)

    def add_vpc_network(self, req=None, **kwargs):
        """ AddVPCNetwork - 添加VPC网段

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Network** (list) - (Required) 增加网段
        - **VPCId** (str) - (Required) 源VPC短ID

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AddVPCNetworkRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("AddVPCNetwork", d, **kwargs)
        return apis.AddVPCNetworkResponseSchema().loads(resp)

    def associate_route_table(self, req=None, **kwargs):
        """ AssociateRouteTable - 绑定子网的路由表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **RouteTableId** (str) - (Required) 路由表ID，仅限自定义路由表
        - **SubnetId** (str) - (Required) 子网ID

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AssociateRouteTableRequestSchema().dumps(d)
        resp = self.invoke("AssociateRouteTable", d, **kwargs)
        return apis.AssociateRouteTableResponseSchema().loads(resp)

    def clone_route_table(self, req=None, **kwargs):
        """ CloneRouteTable - 根据一张现有路由表复制一张新的路由表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **RouteTableId** (str) - (Required) 被克隆的路由表ID

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CloneRouteTableRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CloneRouteTable", d, **kwargs)
        return apis.CloneRouteTableResponseSchema().loads(resp)

    def create_route_table(self, req=None, **kwargs):
        """ CreateRouteTable - 创建路由表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **VPCId** (str) - (Required) VPC ID
        - **Name** (str) - 路由表名称 Default RouteTable
        - **Remark** (str) - 备注
        - **Tag** (str) - 业务组

        **Response**

        - **RouteTableId** (str) - 路由表ID

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateRouteTableRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateRouteTable", d, **kwargs)
        return apis.CreateRouteTableResponseSchema().loads(resp)

    def create_subnet(self, req=None, **kwargs):
        """ CreateSubnet - 创建子网

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Subnet** (str) - (Required) 子网网络地址，例如192.168.0.0
        - **VPCId** (str) - (Required) VPC资源ID
        - **Netmask** (int) - 子网网络号位数，默认为24
        - **Remark** (str) - 备注
        - **SubnetName** (str) - 子网名称，默认为Subnet
        - **Tag** (str) - 业务组名称，默认为Default

        **Response**

        - **SubnetId** (str) - 子网ID

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateSubnetRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateSubnet", d, **kwargs)
        return apis.CreateSubnetResponseSchema().loads(resp)

    def create_vpc(self, req=None, **kwargs):
        """ CreateVPC - 创建VPC

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Name** (str) - (Required) VPC名称
        - **Network** (list) - (Required) VPC网段
        - **Remark** (str) - 备注
        - **Tag** (str) - 业务组名称
        - **Type** (int) - VPC类型

        **Response**

        - **VPCId** (str) - VPC资源Id

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateVPCRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateVPC", d, **kwargs)
        return apis.CreateVPCResponseSchema().loads(resp)

    def create_vpc_intercom(self, req=None, **kwargs):
        """ CreateVPCIntercom - 新建VPC互通关系

        **Request**

        - **ProjectId** (str) - (Config) 源VPC所在项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 源VPC所在地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **DstVPCId** (str) - (Required) 目的VPC短ID
        - **VPCId** (str) - (Required) 源VPC短ID
        - **DstProjectId** (str) - 目的VPC项目ID。默认与源VPC同项目。
        - **DstRegion** (str) - 目的VPC所在地域，默认与源VPC同地域。

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateVPCIntercomRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateVPCIntercom", d, **kwargs)
        return apis.CreateVPCIntercomResponseSchema().loads(resp)

    def delete_route_table(self, req=None, **kwargs):
        """ DeleteRouteTable - 删除自定义路由表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **RouteTableId** (str) - (Required) 路由ID

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteRouteTableRequestSchema().dumps(d)
        resp = self.invoke("DeleteRouteTable", d, **kwargs)
        return apis.DeleteRouteTableResponseSchema().loads(resp)

    def delete_subnet(self, req=None, **kwargs):
        """ DeleteSubnet - 删除子网

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **SubnetId** (str) - (Required) 子网ID

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteSubnetRequestSchema().dumps(d)
        resp = self.invoke("DeleteSubnet", d, **kwargs)
        return apis.DeleteSubnetResponseSchema().loads(resp)

    def delete_vpc(self, req=None, **kwargs):
        """ DeleteVPC - 删除VPC

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **VPCId** (str) - (Required) VPC资源Id

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteVPCRequestSchema().dumps(d)
        resp = self.invoke("DeleteVPC", d, **kwargs)
        return apis.DeleteVPCResponseSchema().loads(resp)

    def delete_vpc_intercom(self, req=None, **kwargs):
        """ DeleteVPCIntercom - 删除VPC互通关系

        **Request**

        - **ProjectId** (str) - (Config) 源VPC所在项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 源VPC所在地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **DstVPCId** (str) - (Required) 目的VPC短ID
        - **VPCId** (str) - (Required) 源VPC短ID
        - **DstProjectId** (str) - 目的VPC所在项目ID，默认为源VPC所在项目ID
        - **DstRegion** (str) - 目的VPC所在地域，默认为源VPC所在地域

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteVPCIntercomRequestSchema().dumps(d)
        resp = self.invoke("DeleteVPCIntercom", d, **kwargs)
        return apis.DeleteVPCIntercomResponseSchema().loads(resp)

    def describe_route_table(self, req=None, **kwargs):
        """ DescribeRouteTable - 获取路由表详细信息(包括路由策略)

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **BusinessId** (str) - 业务组ID
        - **Limit** (int) - Limit
        - **OffSet** (int) - OffSet
        - **RouteTableId** (str) - 路由表ID
        - **VPCId** (str) - VPC ID

        **Response**

        - **RouteTables** (list) - 见 **RouteTableInfo** 模型定义
        - **TotalCount** (int) - RouteTables字段的数量

        **Response Model**

        **RouteRuleInfo**

        - **DstAddr** (str) - 目的地址，比如10.10.8/24
        - **NexthopId** (str) - 路由下一跳ID，比如uvnet-3eljvj
        - **NexthopType** (str) - 下一跳类型，比如local、vnet
        - **Remark** (str) - 路由规则备注
        - **RouteRuleId** (str) - 规则ID
        - **RuleType** (int) - 路由规则类型（0表示系统路由，1表示自定义路由）

        **RouteTableInfo**

        - **CreateTime** (int) - 创建时间戳
        - **Remark** (str) - 路由表备注
        - **RouteRules** (list) - 见 **RouteRuleInfo** 模型定义
        - **RouteTableId** (str) - 路由表ID
        - **RouteTableType** (int) - 路由表类型，1为默认，0为自定义
        - **SubnetCount** (str) - 绑定了该路由表的子网数量
        - **Tag** (str) - 业务组
        - **VPCId** (str) - 路由表所属vpc
        - **VPCName** (str) - vpc名称

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeRouteTableRequestSchema().dumps(d)
        resp = self.invoke("DescribeRouteTable", d, **kwargs)
        return apis.DescribeRouteTableResponseSchema().loads(resp)

    def describe_subnet(self, req=None, **kwargs):
        """ DescribeSubnet - 获取子网信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **BusinessId** (str) - 业务组
        - **Limit** (int) - 列表长度，默认为20
        - **Offset** (int) - 偏移量，默认为0
        - **RouteTableId** (str) - 路由表Id
        - **ShowAvailableIPs** (bool) - 是否返回子网的可用IP数，true为是，false为否，默认不返回
        - **SubnetId** (str) - 子网id，适用于一次查询一个子网信息
        - **SubnetIds** (list) - 子网id数组，适用于一次查询多个子网信息
        - **Tag** (str) - 业务组名称，默认为Default
        - **VPCId** (str) - VPC资源id

        **Response**

        - **DataSet** (list) - 见 **SubnetInfo** 模型定义
        - **TotalCount** (int) - 子网总数量

        **Response Model**

        **SubnetInfo**

        - **AvailableIPs** (int) - 可用IP数量
        - **CreateTime** (int) - 创建时间
        - **Gateway** (str) - 子网网关
        - **HasNATGW** (bool) - 是否有natgw
        - **IPv6Network** (str) - 子网关联的IPv6网段
        - **Netmask** (str) - 子网掩码
        - **Remark** (str) - 备注
        - **RouteTableId** (str) - 路由表Id
        - **Subnet** (str) - 子网网段
        - **SubnetId** (str) - 子网Id
        - **SubnetName** (str) - 子网名称
        - **SubnetType** (int) - 子网类型
        - **Tag** (str) - 业务组
        - **VPCId** (str) - VPCId
        - **VPCName** (str) - VPC名称
        - **Zone** (str) - 可用区名称

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeSubnetRequestSchema().dumps(d)
        resp = self.invoke("DescribeSubnet", d, **kwargs)
        return apis.DescribeSubnetResponseSchema().loads(resp)

    def describe_vpc(self, req=None, **kwargs):
        """ DescribeVPC - 获取VPC信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Limit** (int) -
        - **Offset** (int) -
        - **Tag** (str) - 业务组名称
        - **VPCIds** (list) - VPCId

        **Response**

        - **DataSet** (list) - 见 **VPCInfo** 模型定义

        **Response Model**

        **VPCNetworkInfo**

        - **Network** (str) - vpc地址空间
        - **SubnetCount** (int) - 地址空间中子网数量

        **VPCInfo**

        - **CreateTime** (int) -
        - **IPv6Network** (str) - VPC关联的IPv6网段
        - **Name** (str) -
        - **Network** (list) -
        - **NetworkInfo** (list) - 见 **VPCNetworkInfo** 模型定义
        - **OperatorName** (str) - VPC关联的IPv6网段所属运营商
        - **SubnetCount** (int) -
        - **Tag** (str) -
        - **UpdateTime** (int) -
        - **VPCId** (str) - VPCId

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVPCRequestSchema().dumps(d)
        resp = self.invoke("DescribeVPC", d, **kwargs)
        return apis.DescribeVPCResponseSchema().loads(resp)

    def describe_vpc_intercom(self, req=None, **kwargs):
        """ DescribeVPCIntercom - 获取VPC互通信息

        **Request**

        - **ProjectId** (str) - (Config) 源VPC所在项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 源VPC所在地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **VPCId** (str) - (Required) VPC短ID
        - **DstProjectId** (str) - 目的项目ID，默认为全部项目
        - **DstRegion** (str) - 目的VPC所在地域，默认为全部地域

        **Response**

        - **DataSet** (list) - 见 **VPCIntercomInfo** 模型定义

        **Response Model**

        **VPCIntercomInfo**

        - **DstRegion** (str) - 所属地域
        - **Name** (str) - VPC名字
        - **Network** (list) - VPC的地址空间
        - **ProjectId** (str) - 项目Id
        - **Tag** (str) - 业务组（未分组显示为 Default）
        - **VPCId** (str) - VPCId

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVPCIntercomRequestSchema().dumps(d)
        resp = self.invoke("DescribeVPCIntercom", d, **kwargs)
        return apis.DescribeVPCIntercomResponseSchema().loads(resp)

    def modify_route_rule(self, req=None, **kwargs):
        """ ModifyRouteRule - 路由策略增、删、改

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **RouteRule** (list) - (Required) 格式: RouteRuleId | 目的网段 | 下一跳类型 | 下一跳 |优先级| 备注 | 增、删、改标志  (下一跳类型为instance或者vip，下一跳为云主机id或者vip的id，优先级使用0，动作标志为add/delete/update)   。"添加"示例: test_id | 10.8.0.0/16 | instance | uhost-xd8ja | 0 | Default Route Rule| add (添加的RouteRuleId填任意非空字符串)     。"删除"示例: routerule-xk3jxa | 10.8.0.0/16 | instance | uhost-xd8ja | 0 | Default Route Rule| delete (RouteRuleId来自DescribeRouteTable中)     。“修改”示例: routerule-xk3jxa | 10.8.0.0/16 | instance | uhost-cjksa2 | 0 | Default Route Rule| update (RouteRuleId来自DescribeRouteTable中)
        - **RouteTableId** (str) - (Required) 通过DescribeRouteTable拿到

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyRouteRuleRequestSchema().dumps(d)
        resp = self.invoke("ModifyRouteRule", d, **kwargs)
        return apis.ModifyRouteRuleResponseSchema().loads(resp)

    def update_route_table_attribute(self, req=None, **kwargs):
        """ UpdateRouteTableAttribute - 更新路由表基本信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **RouteTableId** (str) - (Required) 路由表ID
        - **Name** (str) - 名称
        - **Remark** (str) - 备注
        - **Tag** (str) - 业务组名称

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateRouteTableAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateRouteTableAttribute", d, **kwargs)
        return apis.UpdateRouteTableAttributeResponseSchema().loads(resp)

    def update_subnet_attribute(self, req=None, **kwargs):
        """ UpdateSubnetAttribute - 更新子网信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **SubnetId** (str) - (Required) 子网ID
        - **Name** (str) - 子网名称(如果Name不填写，Tag必须填写)
        - **Tag** (str) - 业务组名称(如果Tag不填写，Name必须填写)

        **Response**


        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateSubnetAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateSubnetAttribute", d, **kwargs)
        return apis.UpdateSubnetAttributeResponseSchema().loads(resp)

    def update_vpc_network(self, req=None, **kwargs):
        """ UpdateVPCNetwork - 更新VPC网段

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Network** (list) - (Required) 需要保留的VPC网段。当前仅支持删除VPC网段，添加网段请参考 `AddVPCNetwork <https://docs.ucloud.cn/api/vpc2.0-api/add_vpc_network>`_
        - **VPCId** (str) - (Required) VPC的ID

        **Response**

        - **Message** (str) - 错误信息

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateVPCNetworkRequestSchema().dumps(d)
        resp = self.invoke("UpdateVPCNetwork", d, **kwargs)
        return apis.UpdateVPCNetworkResponseSchema().loads(resp)
