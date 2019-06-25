# -*- coding: utf-8 -*-

from ucloud.core.client import Client
from ucloud.services.uphost.schemas import apis


class UPHostClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(UPHostClient, self).__init__(config, transport, middleware, logger)

    def create_phost(self, req=None, **kwargs):
        """ CreatePHost - 指定数据中心，根据资源使用量创建指定数量的UPHost物理云主机实例。

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ImageId** (str) - (Required) 镜像ID。 请通过 [DescribePHostImage]获取
        - **Password** (str) - (Required) 密码（密码需使用base64进行编码）
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - 计费模式，枚举值为：year, 按年付费； month,按月付费；dynamic，按需付费，（需开启权限） trial, 试用（需开启权限）。默认为按月付费
        - **Cluster** (str) - 网络环境，可选千兆：1G ，万兆：10G， 默认1G
        - **Count** (int) - 购买数量，默认为1，（暂不支持）
        - **CouponId** (str) - 代金券
        - **Name** (str) - 物理机名称，默认为phost
        - **Quantity** (str) - 购买时长，默认为1，范围[1-10]
        - **Raid** (str) - Raid配置，默认Raid10  支持:Raid0、Raid1、Raid5、Raid10，NoRaid
        - **Remark** (str) - 物理机备注，默认为空
        - **SecurityGroupId** (str) - 防火墙Id，默认：Web推荐防火墙。如何查询SecurityGroupId请参见  `DescribeSecurityGroup <https://docs.ucloud.cn/api/unet-api/describe_security_group.html>`_ 
        - **SubnetId** (str) - 子网ID，不填为默认，VPC2.0下需要填写此字段。
        - **Tag** (str) - 业务组，默认为default
        - **Type** (str) - 物理机类型，默认为：db-2(基础型-SAS-V3)
        - **VPCId** (str) - VPC ID，不填为默认，VPC2.0下需要填写此字段。
        
        **Response**

        - **PHostId** (list) - PHost的资源ID数组
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreatePHostRequestSchema().dumps(d)
        resp = self.invoke("CreatePHost", d, **kwargs)
        return apis.CreatePHostResponseSchema().loads(resp)

    def describe_phost(self, req=None, **kwargs):
        """ DescribePHost - 获取物理机详细信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - 返回数据长度，默认为20
        - **Offset** (int) - 数据偏移量，默认为0
        - **PHostId** (list) - PHost资源ID，若为空，则返回当前Region所有PHost。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - 满足条件的PHost总数
        - **PHostSet** (list) - 见 **PHostSet** 模型定义
        
        **Response Model**
        
        **PHostCPUSet** 
        
        - **Count** (int) - CPU个数
        - **CoreCount** (int) - CPU核数
        - **Model** (str) - CPU型号
        - **Frequence** (float) - CPU主频

        **PHostIPSet** 
        
        - **MACAddr** (str) - MAC地址
        - **Bandwidth** (int) - IP对应带宽，单位Mb，内网IP不显示带宽信息
        - **SubnetId** (str) - 子网ID
        - **VPCId** (str) - VPC ID
        - **OperatorName** (str) - 国际: Internation， BGP: BGP， 内网: Private
        - **IPId** (str) - IP资源ID(内网IP无资源ID)（待废弃）
        - **IPAddr** (str) - IP地址，

        **PHostDiskSet** 
        
        - **Space** (int) - 单盘大小，单位GB
        - **Count** (int) - 磁盘数量
        - **Type** (str) - 磁盘属性
        - **Name** (str) - 磁盘名称，sys/data
        - **IOCap** (int) - 磁盘IO性能，单位MB/s（待废弃）

        **PHostSet** 
        
        - **SN** (str) - 物理机序列号
        - **Remark** (str) - 物理机备注
        - **Tag** (str) - 业务组
        - **PowerState** (str) - 电源状态，on 或 off
        - **PHostType** (str) - 物理机类型，参见DescribePHostMachineType返回值
        - **Cluster** (str) - 网络环境。枚举值：千兆：1G ，万兆：10G
        - **IsSupportKVM** (str) - 是否支持紧急登录
        - **CreateTime** (int) - 创建时间
        - **ExpireTime** (int) - 到期时间
        - **Memory** (int) - 内存大小，单位：MB
        - **DiskSet** (list) - 见 **PHostDiskSet** 模型定义
        - **Components** (str) - 组件信息（暂不支持）
        - **RaidSupported** (str) - 是否支持Raid。枚举值：Yes：支持；No：不支持。
        - **Zone** (str) - 可用区，参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PMStatus** (str) - 物理云主机状态。枚举值：\\ > 初始化:Initializing; \\ > 启动中：Starting； \\ > 运行中：Running；\\ > 关机中：Stopping； \\ > 安装失败：InstallFailed； \\ > 重启中：Rebooting；\\ > 关机：Stopped；
        - **OSname** (str) - 操作系统名称
        - **IPSet** (list) - 见 **PHostIPSet** 模型定义
        - **AutoRenew** (str) - 自动续费
        - **PHostId** (str) - PHost资源ID
        - **Name** (str) - 物理机名称
        - **ImageName** (str) - 镜像名称
        - **ChargeType** (str) - 计费模式，枚举值为： Year，按年付费； Month，按月付费； Dynamic，按需付费（需开启权限）； Trial，试用（需开启权限）默认为月付
        - **CPUSet** (list) - 见 **PHostCPUSet** 模型定义
        - **OSType** (str) - 操作系统类型

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostRequestSchema().dumps(d)
        resp = self.invoke("DescribePHost", d, **kwargs)
        return apis.DescribePHostResponseSchema().loads(resp)

    def describe_phost_image(self, req=None, **kwargs):
        """ DescribePHostImage - 获取物理云主机镜像列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ImageId** (list) - 镜像ID
        - **ImageType** (str) - 镜像类别，枚举为：Base,标准镜像；默认为标准镜像。
        - **Limit** (int) - 返回数据长度，默认为20
        - **Offset** (int) - 数据偏移量，默认为0
        
        **Response**

        - **TotalCount** (int) - 满足条件的镜像总数
        - **ImageSet** (list) - 见 **PHostImageSet** 模型定义
        
        **Response Model**
        
        **PHostImageSet** 
        
        - **ImageId** (str) - 镜像ID
        - **ImageName** (str) - 镜像名称
        - **OsName** (str) - 操作系统名称
        - **OsType** (str) - 操作系统类型

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostImageRequestSchema().dumps(d)
        resp = self.invoke("DescribePHostImage", d, **kwargs)
        return apis.DescribePHostImageResponseSchema().loads(resp)

    def describe_phost_tags(self, req=None, **kwargs):
        """ DescribePHostTags - 获取物理机tag列表（业务组）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - Tag的个数
        - **TagSet** (list) - 见 **PHostTagSet** 模型定义
        
        **Response Model**
        
        **PHostTagSet** 
        
        - **Tag** (str) - 业务组名称
        - **TotalCount** (int) - 该业务组中包含的主机个数

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribePHostTagsRequestSchema().dumps(d)
        resp = self.invoke("DescribePHostTags", d, **kwargs)
        return apis.DescribePHostTagsResponseSchema().loads(resp)

    def get_phost_price(self, req=None, **kwargs):
        """ GetPHostPrice - 获取物理机价格列表

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - (Required) 计费模式，枚举值为： Year/Month/Trial/Dynamic
        - **Count** (int) - (Required) 购买数量，范围[1-5]
        - **Quantity** (int) - (Required) 购买时长，1-10个月或1-10年
        - **Cluster** (str) - 网络环境，可选千兆：1G ，万兆：10G
        - **Type** (str) - 默认为：DB(数据库型)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **PriceSet** (list) - 见 **PHostPriceSet** 模型定义
        
        **Response Model**
        
        **PHostPriceSet** 
        
        - **Price** (float) - 价格, 单位:元, 保留小数点后两位有效数字
        - **ChargeType** (str) - Year/Month/Trial/Dynamic

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetPHostPriceRequestSchema().dumps(d)
        resp = self.invoke("GetPHostPrice", d, **kwargs)
        return apis.GetPHostPriceResponseSchema().loads(resp)

    def modify_phost_info(self, req=None, **kwargs):
        """ ModifyPHostInfo - 更改物理机信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PHostId** (str) - (Required) 物理机资源ID
        - **Name** (str) - 物理机名称，默认不更改
        - **Remark** (str) - 物理机备注，默认不更改
        - **Tag** (str) - 业务组，默认不更改
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **PHostId** (str) - PHost 的资源ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyPHostInfoRequestSchema().dumps(d)
        resp = self.invoke("ModifyPHostInfo", d, **kwargs)
        return apis.ModifyPHostInfoResponseSchema().loads(resp)

    def poweroff_phost(self, req=None, **kwargs):
        """ PoweroffPHost - 断电物理云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **PHostId** (str) - PHost 的资源ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.PoweroffPHostRequestSchema().dumps(d)
        resp = self.invoke("PoweroffPHost", d, **kwargs)
        return apis.PoweroffPHostResponseSchema().loads(resp)

    def reboot_phost(self, req=None, **kwargs):
        """ RebootPHost - 重启物理机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **PHostId** (str) - PHost 的资源ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RebootPHostRequestSchema().dumps(d)
        resp = self.invoke("RebootPHost", d, **kwargs)
        return apis.RebootPHostResponseSchema().loads(resp)

    def reinstall_phost(self, req=None, **kwargs):
        """ ReinstallPHost - 重装物理机操作系统

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PHostId** (str) - (Required) PHost资源ID
        - **Password** (str) - (Required) 密码
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ImageId** (str) - 镜像Id，参考镜像列表，默认使用原镜像
        - **Name** (str) - 物理机名称，默认不更改
        - **Raid** (str) - 不保留数据盘重装，可选Raid
        - **Remark** (str) - 物理机备注，默认为不更改。
        - **ReserveDisk** (str) - 是否保留数据盘，保留：Yes，不报留：No， 默认：Yes
        - **Tag** (str) - 业务组，默认不更改。
        
        **Response**

        - **PHostId** (str) - PHost 的资源ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReinstallPHostRequestSchema().dumps(d)
        resp = self.invoke("ReinstallPHost", d, **kwargs)
        return apis.ReinstallPHostResponseSchema().loads(resp)

    def start_phost(self, req=None, **kwargs):
        """ StartPHost - 启动物理机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PHostId** (str) - (Required) PHost资源ID
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **PHostId** (str) - PHost 的资源ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.StartPHostRequestSchema().dumps(d)
        resp = self.invoke("StartPHost", d, **kwargs)
        return apis.StartPHostResponseSchema().loads(resp)

    def terminate_phost(self, req=None, **kwargs):
        """ TerminatePHost - 删除物理云主机

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **PHostId** (str) - (Required) PHost资源ID
        - **ReleaseEIP** (bool) - 是否释放绑定的EIP。true: 解绑EIP后，并释放；其他值或不填：解绑EIP。
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **PHostId** (str) - PHost 的资源ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.TerminatePHostRequestSchema().dumps(d)
        resp = self.invoke("TerminatePHost", d, **kwargs)
        return apis.TerminatePHostResponseSchema().loads(resp)
