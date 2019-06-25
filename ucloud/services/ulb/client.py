# -*- coding: utf-8 -*-

from ucloud.core.client import Client
from ucloud.services.ulb.schemas import apis


class ULBClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(ULBClient, self).__init__(config, transport, middleware, logger)

    def allocate_backend(self, req=None, **kwargs):
        """ AllocateBackend - 添加ULB后端资源实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ResourceId** (str) - (Required) 所添加的后端资源的资源ID
        - **ResourceType** (str) - (Required) 所添加的后端资源的类型，枚举值：UHost -> 云主机；UPM -> 物理云主机； UDHost -> 私有专区主机；UDocker -> 容器，默认值为“UHost”
        - **ULBId** (str) - (Required) 负载均衡实例的ID
        - **VServerId** (str) - (Required) VServer实例的ID
        - **Enabled** (int) - 后端实例状态开关，枚举值： 1：启用； 0：禁用 默认为启用
        - **Port** (int) - 所添加的后端资源服务端口，取值范围[1-65535]，默认80
        - **Weight** (int) - 所添加的后端RS权重（在加权轮询算法下有效），取值范围[0-100]，默认为1
        
        **Response**

        - **BackendId** (str) - 所添加的后端资源在ULB中的对象ID，（为ULB系统中使用，与资源自身ID无关），可用于 UpdateBackendAttribute/UpdateBackendAttributeBatch/ReleaseBackend
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateBackendRequestSchema().dumps(d)
        resp = self.invoke("AllocateBackend", d, **kwargs)
        return apis.AllocateBackendResponseSchema().loads(resp)

    def allocate_backend_batch(self, req=None, **kwargs):
        """ AllocateBackendBatch - 批量添加VServer后端节点

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Backends** (list) - (Required) 用| 分割字段，格式：ResourceId| ResourceType| Port| Enabled|IP| Weight。ResourceId:所添加的后端资源的资源ID；ResourceType:所添加的后端资源的类型，枚举值：UHost -> 云主机；UPM -> 物理云主机； UDHost -> 私有专区主机；UDocker -> 容器，默认值为“UHost”；Port:所添加的后端资源服务端口，取值范围[1-65535]；Enabled:后端实例状态开关，枚举值： 1：启用； 0：禁用；IP:后端资源内网ip；Weight：所添加的后端RS权重（在加权轮询算法下有效），取值范围[0-100]，默认为1
        - **ULBId** (str) - (Required) 负载均衡实例的ID
        - **VServerId** (str) - (Required) VServer实例的ID
        - **ApiVersion** (int) - 
        
        **Response**

        - **BackendSet** (list) - 见 **BackendSet** 模型定义
        
        **Response Model**
        
        **BackendSet** 
        
        - **BackendId** (str) - rs的资源ID
        - **ResourceId** (str) - rs对应的UHost ID

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateBackendBatchRequestSchema().dumps(d)
        resp = self.invoke("AllocateBackendBatch", d, **kwargs)
        return apis.AllocateBackendBatchResponseSchema().loads(resp)

    def bind_ssl(self, req=None, **kwargs):
        """ BindSSL - 将SSL证书绑定到VServer

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SSLId** (str) - (Required) SSL证书的Id
        - **ULBId** (str) - (Required) 所绑定ULB实例ID
        - **VServerId** (str) - (Required) 所绑定VServer实例ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.BindSSLRequestSchema().dumps(d)
        resp = self.invoke("BindSSL", d, **kwargs)
        return apis.BindSSLResponseSchema().loads(resp)

    def create_policy(self, req=None, **kwargs):
        """ CreatePolicy - 创建VServer内容转发策略

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackendId** (list) - (Required) 内容转发策略应用的后端资源实例的ID，来源于 AllocateBackend 返回的 BackendId
        - **Match** (str) - (Required) 内容转发匹配字段
        - **ULBId** (str) - (Required) 需要添加内容转发策略的负载均衡实例ID
        - **VServerId** (str) - (Required) 需要添加内容转发策略的VServer实例ID
        - **Type** (str) - 内容转发匹配字段的类型
        
        **Response**

        - **PolicyId** (str) - 内容转发策略ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreatePolicyRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreatePolicy", d, **kwargs)
        return apis.CreatePolicyResponseSchema().loads(resp)

    def create_ssl(self, req=None, **kwargs):
        """ CreateSSL - 创建SSL证书，可以把整个 Pem 证书内容传过来，或者把证书、私钥、CA证书分别传过来

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SSLName** (str) - (Required) SSL证书的名字，默认值为空
        - **CaCert** (str) - CA证书
        - **PrivateKey** (str) - 加密证书的私钥
        - **SSLContent** (str) - SSL证书的完整内容，包括用户证书、加密证书的私钥、CA证书
        - **SSLType** (str) - 所添加的SSL证书类型，目前只支持Pem格式
        - **UserCert** (str) - 用户的证书
        
        **Response**

        - **SSLId** (str) - SSL证书的Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateSSLRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateSSL", d, **kwargs)
        return apis.CreateSSLResponseSchema().loads(resp)

    def create_ulb(self, req=None, **kwargs):
        """ CreateULB - 创建负载均衡实例，可以选择内网或者外网

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BusinessId** (str) - ULB 所属的业务组ID，如果不传则使用默认的业务组
        - **ChargeType** (str) - 付费方式
        - **IPVersion** (str) - ULB ip类型，枚举值：IPv6 / IPv4 （内部测试，暂未对外开放）
        - **InnerMode** (str) - 创建的ULB是否为内网模式
        - **ListenType** (str) - ULB 监听器类型，枚举值：RequestProxy / PacketsTransmit （内部测试，暂未对外开放）
        - **OuterMode** (str) - 创建的ULB是否为外网模式，默认即为外网模式
        - **PrivateIp** (str) - 创建内网ULB时指定内网IP。若不传值，则随机分配当前子网下的IP（暂时不对外开放，创建外网ULB该字段会忽略）
        - **Remark** (str) - 备注
        - **SubnetId** (str) - 内网ULB 所属的子网ID，如果不传则使用默认的子网
        - **Tag** (str) - 业务组
        - **ULBName** (str) - 负载均衡的名字，默认值为“ULB”
        - **VPCId** (str) - ULB所在的VPC的ID, 如果不传则使用默认的VPC
        
        **Response**

        - **ULBId** (str) - 负载均衡实例的Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateULBRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateULB", d, **kwargs)
        return apis.CreateULBResponseSchema().loads(resp)

    def create_vserver(self, req=None, **kwargs):
        """ CreateVServer - 创建VServer实例，定义监听的协议和端口以及负载均衡算法

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ULBId** (str) - (Required) 负载均衡实例ID
        - **ClientTimeout** (int) - ListenType为RequestProxy时表示空闲连接的回收时间，单位：秒，取值范围：时(0，86400]，默认值为60；ListenType为PacketsTransmit时表示连接保持的时间，单位：秒，取值范围：[60，900]，0 表示禁用连接保持
        - **Domain** (str) - 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查路径
        - **FrontendPort** (int) - VServer后端端口，取值范围[1-65535]；默认值为80
        - **ListenType** (str) - 监听器类型，枚举值为：RequestProxy -> 请求代理；PacketsTransmit -> 报文转发；默认为"RequestProxy"
        - **Method** (str) - VServer负载均衡模式，枚举值：Roundrobin -> 轮询;Source -> 源地址；ConsistentHash -> 一致性哈希；SourcePort -> 源地址（计算端口）；ConsistentHashPort -> 一致性哈希（计算端口）; WeightRoundrobin -> 加权轮询; Leastconn -> 最小连接数。ConsistentHash，SourcePort，ConsistentHashPort 只在报文转发中使用；Leastconn只在请求代理中使用；Roundrobin、Source和WeightRoundrobin在请求代理和报文转发中使用。默认为："Roundrobin"
        - **MonitorType** (str) - 健康检查类型，枚举值：Port -> 端口检查；Path -> 路径检查；
        - **Path** (str) - 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查域名
        - **PersistenceInfo** (str) - 根据PersistenceType确认； None和ServerInsert： 此字段无意义； UserDefined：此字段传入自定义会话保持String
        - **PersistenceType** (str) - VServer会话保持方式，默认关闭会话保持。枚举值：None -> 关闭；ServerInsert -> 自动生成KEY；UserDefined -> 用户自定义KEY。
        - **Protocol** (str) - VServer实例的协议，请求代理模式下有 HTTP、HTTPS、TCP，报文转发下有 TCP，UDP。默认为“HTTP"
        - **VServerName** (str) - VServer实例名称，默认为"VServer"
        
        **Response**

        - **VServerId** (str) - VServer实例的Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateVServerRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateVServer", d, **kwargs)
        return apis.CreateVServerResponseSchema().loads(resp)

    def delete_policy(self, req=None, **kwargs):
        """ DeletePolicy - 删除内容转发策略

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PolicyId** (str) - (Required) 内容转发策略ID
        - **GroupId** (str) - 内容转发策略组ID
        - **VServerId** (str) - VServer 资源ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeletePolicyRequestSchema().dumps(d)
        resp = self.invoke("DeletePolicy", d, **kwargs)
        return apis.DeletePolicyResponseSchema().loads(resp)

    def delete_ssl(self, req=None, **kwargs):
        """ DeleteSSL - 删除SSL证书

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SSLId** (str) - (Required) SSL证书的ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteSSLRequestSchema().dumps(d)
        resp = self.invoke("DeleteSSL", d, **kwargs)
        return apis.DeleteSSLResponseSchema().loads(resp)

    def delete_ulb(self, req=None, **kwargs):
        """ DeleteULB - 删除负载均衡实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ULBId** (str) - (Required) 负载均衡实例的ID
        - **ReleaseEip** (bool) - 删除ulb时是否释放绑定的EIP，false标识只解绑EIP，true表示会释放绑定的EIP，默认是false
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteULBRequestSchema().dumps(d)
        resp = self.invoke("DeleteULB", d, **kwargs)
        return apis.DeleteULBResponseSchema().loads(resp)

    def delete_vserver(self, req=None, **kwargs):
        """ DeleteVServer - 删除VServer实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ULBId** (str) - (Required) 负载均衡实例的ID
        - **VServerId** (str) - (Required) VServer实例的ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteVServerRequestSchema().dumps(d)
        resp = self.invoke("DeleteVServer", d, **kwargs)
        return apis.DeleteVServerResponseSchema().loads(resp)

    def describe_ssl(self, req=None, **kwargs):
        """ DescribeSSL - 获取SSL证书信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - 数据分页值，默认为20
        - **Offset** (int) - 数据偏移量，默认值为0
        - **SSLId** (str) - SSL证书的Id
        
        **Response**

        - **TotalCount** (int) - 满足条件的SSL证书总数
        - **DataSet** (list) - 见 **ULBSSLSet** 模型定义
        
        **Response Model**
        
        **ULBSSLSet** 
        
        - **SSLName** (str) - SSL证书的名字
        - **HashValue** (str) - 
        - **SSLId** (str) - SSL证书的Id

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeSSLRequestSchema().dumps(d)
        resp = self.invoke("DescribeSSL", d, **kwargs)
        return apis.DescribeSSLResponseSchema().loads(resp)

    def describe_ulb(self, req=None, **kwargs):
        """ DescribeULB - 获取ULB详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BusinessId** (str) - ULB所属的业务组ID
        - **Limit** (int) - 数据分页值，默认为20
        - **Offset** (int) - 数据偏移量，默认为0
        - **SubnetId** (str) - ULB所属的子网ID
        - **ULBId** (str) - 负载均衡实例的Id。 若指定则返回指定的负载均衡实例的信息； 若不指定则返回当前数据中心中所有的负载均衡实例的信息
        - **VPCId** (str) - ULB所属的VPC
        
        **Response**

        - **TotalCount** (int) - 满足条件的ULB总数
        - **DataSet** (list) - 见 **ULBSet** 模型定义
        
        **Response Model**
        
        **PolicyBackendSet** 
        
        - **PrivateIP** (str) - 后端资源的内网IP
        - **ResourceName** (str) - 后端资源的实例名称
        - **BackendId** (str) - 所添加的后端资源在ULB中的对象ID，（为ULB系统中使用，与资源自身ID无关
        - **ObjectId** (str) - 后端资源的对象ID
        - **Port** (int) - 所添加的后端资源服务端口

        **ULBPolicySet** 
        
        - **PolicyId** (str) - 内容转发Id，默认内容转发类型下为空。
        - **PolicyType** (str) - 内容类型，枚举值：Custom -> 客户自定义；Default -> 默认内容转发
        - **Type** (str) - 内容转发匹配字段的类型，枚举值：Domain -> 域名；Path -> 路径； 默认内容转发类型下为空
        - **Match** (str) - 内容转发匹配字段;默认内容转发类型下为空。
        - **PolicyPriority** (int) - 内容转发优先级，范围[1,9999]，数字越大优先级越高。默认内容转发规则下为0。
        - **VServerId** (str) - 所属VServerId
        - **TotalCount** (int) - 默认内容转发类型下返回当前rs总数
        - **BackendSet** (list) - 见 **PolicyBackendSet** 模型定义

        **ULBBackendSet** 
        
        - **ResourceId** (str) - 资源实例的资源Id
        - **SubResourceId** (str) - 资源绑定的虚拟网卡实例的资源Id
        - **SubResourceName** (str) - 资源绑定的虚拟网卡实例的资源名称
        - **SubnetId** (str) - 后端提供服务的资源所在的子网的ID
        - **PrivateIP** (str) - 后端提供服务的内网IP
        - **Port** (int) - 后端提供服务的端口
        - **Enabled** (int) - 后端提供服务的实例启用与否，枚举值：0 禁用 1 启用
        - **Status** (int) - 后端提供服务的实例运行状态，枚举值：0健康检查健康状态 1 健康检查异常
        - **BackendId** (str) - 后端资源实例的Id
        - **ResourceType** (str) - 资源实例的类型
        - **ResourceName** (str) - 资源实例的资源名称
        - **SubResourceType** (str) - 资源绑定的虚拟网卡实例的类型
        - **Weight** (int) - 

        **ULBSSLSet** 
        
        - **SSLId** (str) - SSL证书的Id
        - **SSLName** (str) - SSL证书的名字
        - **HashValue** (str) - 

        **ULBVServerSet** 
        
        - **Path** (str) - 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查域名
        - **ClientTimeout** (int) - 空闲连接的回收时间，单位：秒。
        - **VServerId** (str) - VServer实例的Id
        - **Protocol** (str) - VServer实例的协议。 枚举值为：HTTP，TCP，UDP，HTTPS。
        - **PersistenceInfo** (str) - 根据PersistenceType确定： None或ServerInsert，此字段为空； UserDefined，此字段展示用户自定义会话string。
        - **Method** (str) - VServer负载均衡的模式，枚举值：Roundrobin -> 轮询;Source -> 源地址；ConsistentHash -> 一致性哈希；SourcePort -> 源地址（计算端口）；ConsistentHashPort -> 一致性哈希（计算端口）。
        - **PersistenceType** (str) - VServer会话保持方式。枚举值为： None -> 关闭会话保持； ServerInsert -> 自动生成； UserDefined -> 用户自定义。
        - **Status** (int) - VServer的运行状态。枚举值： 0 -> rs全部运行正常;1 -> rs全部运行异常；2 -> rs部分运行异常。
        - **SSLSet** (list) - 见 **ULBSSLSet** 模型定义
        - **BackendSet** (list) - 见 **ULBBackendSet** 模型定义
        - **MonitorType** (str) - 健康检查类型，枚举值：Port -> 端口检查；Path -> 路径检查；
        - **VServerName** (str) - VServer实例的名字
        - **FrontendPort** (int) - VServer服务端口
        - **Domain** (str) - 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查路径
        - **ListenType** (str) - 监听器类型，枚举值为: RequestProxy -> 请求代理；PacketsTransmit -> 报文转发
        - **PolicySet** (list) - 见 **ULBPolicySet** 模型定义

        **ULBIPSet** 
        
        - **BandwidthType** (int) - 弹性IP的带宽类型，枚举值：1 表示是共享带宽，0 普通带宽类型（暂未对外开放）
        - **Bandwidth** (int) - 弹性IP的带宽值（暂未对外开放）
        - **OperatorName** (str) - 弹性IP的运营商信息，枚举值为：  Bgp：BGP IP International：国际IP
        - **EIP** (str) - 弹性IP地址
        - **EIPId** (str) - 弹性IP的ID

        **ULBSet** 
        
        - **Tag** (str) - 负载均衡的业务组名称，缺省值“Default”
        - **Bandwidth** (int) - 带宽
        - **CreateTime** (int) - ULB的创建时间，格式为Unix Timestamp
        - **ExpireTime** (int) - ULB的到期时间，格式为Unix Timestamp
        - **Resource** (list) - ULB的详细信息列表（废弃）
        - **VPCId** (str) - ULB所在的VPC的ID
        - **SubnetId** (str) - ULB 为 InnerMode 时，ULB 所属的子网ID，默认为空
        - **PrivateIP** (str) - ULB的内网IP，当ULBType为OuterMode时，该值为空
        - **Remark** (str) - 负载均衡的备注，缺省值“”
        - **BandwidthType** (int) - 带宽类型，枚举值为： 0，非共享带宽； 1，共享带宽
        - **IPSet** (list) - 见 **ULBIPSet** 模型定义
        - **VServerSet** (list) - 见 **ULBVServerSet** 模型定义
        - **ULBType** (str) - ULB 的类型
        - **BusinessId** (str) - ULB 所属的业务组ID
        - **ULBId** (str) - 负载均衡的资源ID
        - **ULBName** (str) - 负载均衡的资源名称(内部记载，废弃)
        - **Name** (str) - 负载均衡的资源名称（资源系统中），缺省值“ULB”

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeULBRequestSchema().dumps(d)
        resp = self.invoke("DescribeULB", d, **kwargs)
        return apis.DescribeULBResponseSchema().loads(resp)

    def describe_vserver(self, req=None, **kwargs):
        """ DescribeVServer - 获取ULB下的VServer的详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ULBId** (str) - (Required) 负载均衡实例的Id
        - **Limit** (int) - 数据分页值
        - **Offset** (int) - 数据偏移量
        - **VServerId** (str) - VServer实例的Id；若指定则返回指定的VServer实例的信息； 若不指定则返回当前负载均衡实例下所有VServer的信息
        
        **Response**

        - **TotalCount** (int) - 满足条件的VServer总数
        - **DataSet** (list) - 见 **ULBVServerSet** 模型定义
        
        **Response Model**
        
        **PolicyBackendSet** 
        
        - **ObjectId** (str) - 后端资源的对象ID
        - **Port** (int) - 所添加的后端资源服务端口
        - **PrivateIP** (str) - 后端资源的内网IP
        - **ResourceName** (str) - 后端资源的实例名称
        - **BackendId** (str) - 所添加的后端资源在ULB中的对象ID，（为ULB系统中使用，与资源自身ID无关

        **ULBBackendSet** 
        
        - **ResourceId** (str) - 资源实例的资源Id
        - **SubResourceId** (str) - 资源绑定的虚拟网卡实例的资源Id
        - **SubResourceName** (str) - 资源绑定的虚拟网卡实例的资源名称
        - **SubnetId** (str) - 后端提供服务的资源所在的子网的ID
        - **Status** (int) - 后端提供服务的实例运行状态，枚举值：0健康检查健康状态 1 健康检查异常
        - **BackendId** (str) - 后端资源实例的Id
        - **ResourceType** (str) - 资源实例的类型
        - **ResourceName** (str) - 资源实例的资源名称
        - **SubResourceType** (str) - 资源绑定的虚拟网卡实例的类型
        - **PrivateIP** (str) - 后端提供服务的内网IP
        - **Port** (int) - 后端提供服务的端口
        - **Enabled** (int) - 后端提供服务的实例启用与否，枚举值：0 禁用 1 启用
        - **Weight** (int) - 

        **ULBSSLSet** 
        
        - **SSLId** (str) - SSL证书的Id
        - **SSLName** (str) - SSL证书的名字
        - **HashValue** (str) - 

        **ULBPolicySet** 
        
        - **Type** (str) - 内容转发匹配字段的类型，枚举值：Domain -> 域名；Path -> 路径； 默认内容转发类型下为空
        - **Match** (str) - 内容转发匹配字段;默认内容转发类型下为空。
        - **PolicyPriority** (int) - 内容转发优先级，范围[1,9999]，数字越大优先级越高。默认内容转发规则下为0。
        - **VServerId** (str) - 所属VServerId
        - **TotalCount** (int) - 默认内容转发类型下返回当前rs总数
        - **BackendSet** (list) - 见 **PolicyBackendSet** 模型定义
        - **PolicyId** (str) - 内容转发Id，默认内容转发类型下为空。
        - **PolicyType** (str) - 内容类型，枚举值：Custom -> 客户自定义；Default -> 默认内容转发

        **ULBVServerSet** 
        
        - **BackendSet** (list) - 见 **ULBBackendSet** 模型定义
        - **MonitorType** (str) - 健康检查类型，枚举值：Port -> 端口检查；Path -> 路径检查；
        - **VServerName** (str) - VServer实例的名字
        - **FrontendPort** (int) - VServer服务端口
        - **Method** (str) - VServer负载均衡的模式，枚举值：Roundrobin -> 轮询;Source -> 源地址；ConsistentHash -> 一致性哈希；SourcePort -> 源地址（计算端口）；ConsistentHashPort -> 一致性哈希（计算端口）。
        - **PersistenceType** (str) - VServer会话保持方式。枚举值为： None -> 关闭会话保持； ServerInsert -> 自动生成； UserDefined -> 用户自定义。
        - **Status** (int) - VServer的运行状态。枚举值： 0 -> rs全部运行正常;1 -> rs全部运行异常；2 -> rs部分运行异常。
        - **SSLSet** (list) - 见 **ULBSSLSet** 模型定义
        - **Domain** (str) - 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查路径
        - **ListenType** (str) - 监听器类型，枚举值为: RequestProxy -> 请求代理；PacketsTransmit -> 报文转发
        - **PolicySet** (list) - 见 **ULBPolicySet** 模型定义
        - **Path** (str) - 根据MonitorType确认； 当MonitorType为Port时，此字段无意义。当MonitorType为Path时，代表HTTP检查域名
        - **VServerId** (str) - VServer实例的Id
        - **Protocol** (str) - VServer实例的协议。 枚举值为：HTTP，TCP，UDP，HTTPS。
        - **PersistenceInfo** (str) - 根据PersistenceType确定： None或ServerInsert，此字段为空； UserDefined，此字段展示用户自定义会话string。
        - **ClientTimeout** (int) - 空闲连接的回收时间，单位：秒。

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeVServerRequestSchema().dumps(d)
        resp = self.invoke("DescribeVServer", d, **kwargs)
        return apis.DescribeVServerResponseSchema().loads(resp)

    def release_backend(self, req=None, **kwargs):
        """ ReleaseBackend - 从VServer释放后端资源实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackendId** (str) - (Required) 后端资源实例的ID(ULB后端ID，非资源自身ID)
        - **ULBId** (str) - (Required) 负载均衡实例的ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseBackendRequestSchema().dumps(d)
        resp = self.invoke("ReleaseBackend", d, **kwargs)
        return apis.ReleaseBackendResponseSchema().loads(resp)

    def unbind_ssl(self, req=None, **kwargs):
        """ UnbindSSL - 从VServer解绑SSL证书

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SSLId** (str) - (Required) SSL证书的Id
        - **ULBId** (str) - (Required) 所绑定ULB实例ID
        - **VServerId** (str) - (Required) 所绑定VServer实例ID
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UnbindSSLRequestSchema().dumps(d)
        resp = self.invoke("UnbindSSL", d, **kwargs)
        return apis.UnbindSSLResponseSchema().loads(resp)

    def update_backend_attribute(self, req=None, **kwargs):
        """ UpdateBackendAttribute - 更新ULB后端资源实例(服务节点)属性

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackendId** (str) - (Required) 后端资源实例的ID(ULB后端ID，非资源自身ID)
        - **ULBId** (str) - (Required) 负载均衡资源ID
        - **Enabled** (int) - 后端实例状态开关
        - **Port** (int) - 后端资源服务端口，取值范围[1-65535]
        - **Weight** (int) - 所添加的后端RS权重（在加权轮询算法下有效），取值范围[0-100]，默认为1
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateBackendAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateBackendAttribute", d, **kwargs)
        return apis.UpdateBackendAttributeResponseSchema().loads(resp)

    def update_policy(self, req=None, **kwargs):
        """ UpdatePolicy - 更新内容转发规则，包括转发规则后的服务节点

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **BackendId** (list) - (Required) 内容转发策略应用的后端资源实例的ID，来源于 AllocateBackend 返回的 BackendId
        - **Match** (str) - (Required) 内容转发匹配字段
        - **PolicyId** (str) - (Required) 转发规则的ID
        - **ULBId** (str) - (Required) 需要添加内容转发策略的负载均衡实例ID
        - **VServerId** (str) - (Required) 需要添加内容转发策略的VServer实例ID
        - **Type** (str) - 内容转发匹配字段的类型
        
        **Response**

        - **PolicyId** (str) - 转发规则的ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdatePolicyRequestSchema().dumps(d)
        resp = self.invoke("UpdatePolicy", d, **kwargs)
        return apis.UpdatePolicyResponseSchema().loads(resp)

    def update_ulb_attribute(self, req=None, **kwargs):
        """ UpdateULBAttribute - 更新ULB名字业务组备注等属性字段

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ULBId** (str) - (Required) ULB资源ID
        - **Name** (str) - 名字
        - **Remark** (str) - 备注
        - **Tag** (str) - 业务
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateULBAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateULBAttribute", d, **kwargs)
        return apis.UpdateULBAttributeResponseSchema().loads(resp)

    def update_vserver_attribute(self, req=None, **kwargs):
        """ UpdateVServerAttribute - 更新VServer实例属性

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ULBId** (str) - (Required) 负载均衡实例ID
        - **VServerId** (str) - (Required) VServer实例ID
        - **ClientTimeout** (int) - 请求代理的VServer下表示空闲连接的回收时间，单位：秒，取值范围：时(0，86400]，默认值为60；报文转发的VServer下表示回话保持的时间，单位：秒，取值范围：[60，900]，0 表示禁用连接保持
        - **Domain** (str) - MonitorType 为 Path 时指定健康检查发送请求时HTTP HEADER 里的域名
        - **Method** (str) - VServer负载均衡模式，枚举值：Roundrobin -> 轮询;Source -> 源地址；ConsistentHash -> 一致性哈希；SourcePort -> 源地址（计算端口）；ConsistentHashPort -> 一致性哈希（计算端口）; WeightRoundrobin -> 加权轮询; Leastconn -> 最小连接数。ConsistentHash，SourcePort，ConsistentHashPort 只在报文转发中使用；Leastconn只在请求代理中使用；Roundrobin、Source和WeightRoundrobin在请求代理和报文转发中使用。默认为："Roundrobin"
        - **MonitorType** (str) - 健康检查的类型，Port:端口,Path:路径
        - **Path** (str) - MonitorType 为 Path 时指定健康检查发送请求时的路径，默认为 /
        - **PersistenceInfo** (str) - 根据PersistenceType确定: None或ServerInsert, 此字段无意义; UserDefined, 则此字段传入用户自定义会话保持String. 若无此字段则不做修改
        - **PersistenceType** (str) - VServer会话保持模式，若无此字段则不做修改。枚举值：None：关闭；ServerInsert：自动生成KEY；UserDefined：用户自定义KEY。
        - **Protocol** (str) - VServer协议类型，请求代理只支持修改为 HTTP/HTTPS，报文转发VServer只支持修改为 TCP/UDP
        - **VServerName** (str) - VServer实例名称，若无此字段则不做修改
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateVServerAttributeRequestSchema().dumps(d)
        resp = self.invoke("UpdateVServerAttribute", d, **kwargs)
        return apis.UpdateVServerAttributeResponseSchema().loads(resp)
