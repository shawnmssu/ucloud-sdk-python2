# -*- coding: utf-8 -*-

from ucloud.core.client import Client
from ucloud.services.udisk.schemas import apis


class UDiskClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(UDiskClient, self).__init__(config, transport, middleware, logger)

    def attach_udisk(self, req=None, **kwargs):
        """ AttachUDisk - 将一个可用的UDisk挂载到某台主机上，当UDisk挂载成功后，还需要在主机内部进行文件系统操作

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDiskId** (str) - (Required) 需要挂载的UDisk实例ID.
        - **UHostId** (str) - (Required) UHost实例ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **MultiAttach** (str) - 是否允许多点挂载（Yes: 允许多点挂载， No: 不允许多点挂载， 不填默认Yes ）
        
        **Response**

        - **UHostId** (str) - 挂载的UHost实例ID
        - **UDiskId** (str) - 挂载的UDisk实例ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AttachUDiskRequestSchema().dumps(d)
        resp = self.invoke("AttachUDisk", d, **kwargs)
        return apis.AttachUDiskResponseSchema().loads(resp)

    def clone_udisk(self, req=None, **kwargs):
        """ CloneUDisk - 从UDisk创建UDisk克隆

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 实例名称
        - **SourceId** (str) - (Required) 克隆父Disk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - Year , Month, Dynamic，Postpay 默认: Dynamic
        - **Comment** (str) - Disk注释
        - **CouponId** (str) - 使用的代金券id
        - **Quantity** (int) - 购买时长 默认: 1
        - **UDataArkMode** (str) - 方舟是否开启，"Yes":开启，"No":关闭；默认为"No"
        
        **Response**

        - **UDiskId** (list) - 创建UDisk Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CloneUDiskRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CloneUDisk", d, **kwargs)
        return apis.CloneUDiskResponseSchema().loads(resp)

    def clone_udisk_snapshot(self, req=None, **kwargs):
        """ CloneUDiskSnapshot - 从快照创建UDisk克隆

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 实例名称
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,范围[1~2000], 权限位控制可达8T,若需要请申请开通相关权限。
        - **SourceId** (str) - (Required) 克隆父Snapshot的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - Year , Month, Dynamic，Postpay 默认: Dynamic
        - **Comment** (str) - Disk注释
        - **CouponId** (str) - 使用的代金券id
        - **Quantity** (int) - 购买时长 默认: 1
        - **UDataArkMode** (str) - 是否开启数据方舟   默认:No
        
        **Response**

        - **UDiskId** (list) - 创建UDisk Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CloneUDiskSnapshotRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CloneUDiskSnapshot", d, **kwargs)
        return apis.CloneUDiskSnapshotResponseSchema().loads(resp)

    def create_udisk(self, req=None, **kwargs):
        """ CreateUDisk - 创建UDisk磁盘

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 实例名称
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,普通盘: 范围[1~2000], 权限位控制可达8T,若需要请申请开通相关权限;SSD盘： 范围[1~4000]。
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - Year , Month, Dynamic, Postpay, Trial 默认: Dynamic
        - **CmkId** (str) - 加密需要的cmk id，UKmsMode为Yes时，必填
        - **CouponId** (str) - 使用的代金券id
        - **DiskType** (str) - UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），RSSDDataDisk（RSSD数据盘），默认值（DataDisk）
        - **Quantity** (int) - 购买时长 默认: 1
        - **Tag** (str) - 业务组 默认：Default
        - **UDataArkMode** (str) - 是否开启数据方舟
        - **UKmsMode** (str) - 是否加密。Yes：加密，No：不加密，默认值（No）
        
        **Response**

        - **UDiskId** (list) - UDisk实例Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDiskRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDisk", d, **kwargs)
        return apis.CreateUDiskResponseSchema().loads(resp)

    def create_udisk_snapshot(self, req=None, **kwargs):
        """ CreateUDiskSnapshot - 创建snapshot快照

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Name** (str) - (Required) 快照名称
        - **UDiskId** (str) - (Required) 快照的UDisk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - Year , Month, Dynamic 默认: Dynamic
        - **Comment** (str) - 快照描述
        - **Quantity** (int) - 购买时长 默认: 1
        
        **Response**

        - **SnapshotId** (list) - 快照Id
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUDiskSnapshotRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateUDiskSnapshot", d, **kwargs)
        return apis.CreateUDiskSnapshotResponseSchema().loads(resp)

    def delete_udisk(self, req=None, **kwargs):
        """ DeleteUDisk - 删除UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDiskId** (str) - (Required) 要删除的UDisk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDiskRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDisk", d, **kwargs)
        return apis.DeleteUDiskResponseSchema().loads(resp)

    def delete_udisk_snapshot(self, req=None, **kwargs):
        """ DeleteUDiskSnapshot - 删除Snapshot

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SnapshotId** (str) - (Required) 快照Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDiskId** (str) - UDisk Id,删除该盘所创建出来的所有快照
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUDiskSnapshotRequestSchema().dumps(d)
        resp = self.invoke("DeleteUDiskSnapshot", d, **kwargs)
        return apis.DeleteUDiskSnapshotResponseSchema().loads(resp)

    def describe_udisk(self, req=None, **kwargs):
        """ DescribeUDisk - 获取UDisk实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DiskType** (str) - 普通数据盘:DataDisk; 普通系统盘:SystemDisk; SSD数据盘:SSDDataDisk; RSSD数据盘:RSSDDataDisk; 为空拉取所有
        - **Limit** (int) - 返回数据长度, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0
        - **UDiskId** (str) - UDisk Id(留空返回全部)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **DataSet** (list) - 见 **UDiskDataSet** 模型定义
        - **TotalCount** (int) - 根据过滤条件得到的总数
        
        **Response Model**
        
        **UDiskDataSet** 
        
        - **CreateTime** (int) - 创建时间
        - **UHostId** (str) - 挂载的UHost的Id
        - **ChargeType** (str) - Year,Month,Dynamic,Trial,Postpay
        - **Status** (str) - 状态:Available(可用),Attaching(挂载中), InUse(已挂载), Detaching(卸载中), Initializating(分配中), Failed(创建失败),Cloning(克隆中),Restoring(恢复中),RestoreFailed(恢复失败),
        - **ExpiredTime** (int) - 过期时间
        - **ArkSwitchEnable** (int) - 是否支持开启方舟，1支持 ，0不支持
        - **CloneEnable** (int) - 是否支持克隆，1支持 ，0不支持
        - **CmkIdStatus** (str) - 该盘cmk的状态, Enabled(正常)，Disabled(失效)，Deleted(删除)，NoCmkId(非加密盘)
        - **Zone** (str) - 可用区
        - **UHostIP** (str) - 挂载的UHost的IP
        - **UDiskId** (str) - UDisk实例Id
        - **IsExpire** (str) - 资源是否过期，过期:"Yes", 未过期:"No"
        - **DiskType** (str) - 云硬盘类型: 普通数据盘:DataDisk,普通系统盘:SystemDisk,SSD数据盘:SSDDataDisk,RSSD数据盘:RSSDDataDisk
        - **SnapEnable** (int) - 是否支持快照，1支持 ，0不支持
        - **UKmsMode** (str) - 是否是加密盘，是:"Yes", 否:"No"
        - **CmkId** (str) - 该盘的cmk id
        - **SnapshotCount** (int) - 该盘快照个数
        - **SnapshotLimit** (int) - 该盘快照上限
        - **Size** (int) - 容量单位GB
        - **Tag** (str) - 业务组名称
        - **Version** (str) - 是否支持数据方舟，支持:"2.0", 不支持:"1.0"
        - **UDataArkMode** (str) - 是否开启数据方舟，开启:"Yes", 不支持:"No"
        - **DataKey** (str) - 该盘的密文密钥
        - **Name** (str) - 实例名称
        - **DeviceName** (str) - 挂载的设备名称
        - **UHostName** (str) - 挂载的UHost的Name
        - **CmkIdAlias** (str) - cmk id 别名

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDisk", d, **kwargs)
        return apis.DescribeUDiskResponseSchema().loads(resp)

    def describe_udisk_price(self, req=None, **kwargs):
        """ DescribeUDiskPrice - 获取UDisk实例价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,范围[1~1000]
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **ChargeType** (str) - Year， Month， Dynamic，Trial，默认: Dynamic 如果不指定，则一次性获取三种计费
        - **DiskType** (str) - UDisk 类型: DataDisk（普通数据盘），SSDDataDisk（SSD数据盘），默认值（DataDisk）
        - **Quantity** (int) - 购买UDisk的时长，默认值为1
        - **UDataArkMode** (str) - 是否打开数据方舟, 打开"Yes",关闭"No", 默认关闭
        
        **Response**

        - **DataSet** (list) - 见 **UDiskPriceDataSet** 模型定义
        
        **Response Model**
        
        **UDiskPriceDataSet** 
        
        - **ChargeName** (str) - "UDataArk","UDisk"
        - **ChargeType** (str) - Year， Month， Dynamic，Trial
        - **Price** (float) - 价格 (单位: 分)

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskPriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDiskPrice", d, **kwargs)
        return apis.DescribeUDiskPriceResponseSchema().loads(resp)

    def describe_udisk_snapshot(self, req=None, **kwargs):
        """ DescribeUDiskSnapshot - 获取UDisk快照

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - 返回数据长度, 默认为20
        - **Offset** (int) - 数据偏移量, 默认为0
        - **SnapshotId** (str) - 快照id，SnapshotId , UDiskId 同时传SnapshotId优先
        - **UDiskId** (str) - UDiskId,返回该盘所做快照.(必须同时传Zone)
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - 根据过滤条件得到的总数
        - **DataSet** (list) - 见 **UDiskSnapshotSet** 模型定义
        
        **Response Model**
        
        **UDiskSnapshotSet** 
        
        - **CmkId** (str) - 该快照的cmk id
        - **CmkIdStatus** (str) - 该快照cmk的状态, Enabled(正常)，Disabled(失效)，Deleted(删除)，NoCmkId(非加密盘)
        - **Name** (str) - 快照名称
        - **UDiskId** (str) - 快照的源UDisk的Id
        - **ExpiredTime** (int) - 过期时间
        - **Size** (int) - 容量单位GB
        - **CmkIdAlias** (str) - cmk id 别名
        - **IsUDiskAvailable** (bool) - 对应磁盘是否处于可用状态
        - **UHostId** (str) - 对应磁盘制作快照时所挂载的主机
        - **DataKey** (str) - 该快照的密文密钥
        - **Status** (str) - 快照状态，Normal:正常,Failed:失败,Creating:制作中
        - **DiskType** (int) - 磁盘类型，0:数据盘，1:系统盘
        - **Comment** (str) - 快照描述
        - **Version** (str) - 快照版本
        - **UKmsMode** (str) - 是否是加密盘快照，是:"Yes", 否:"No"
        - **SnapshotId** (str) - 快照Id
        - **UDiskName** (str) - 快照的源UDisk的Name
        - **CreateTime** (int) - 创建时间

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskSnapshotRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDiskSnapshot", d, **kwargs)
        return apis.DescribeUDiskSnapshotResponseSchema().loads(resp)

    def describe_udisk_upgrade_price(self, req=None, **kwargs):
        """ DescribeUDiskUpgradePrice - 获取UDisk升级价格信息

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 购买UDisk大小,单位:GB,范围[1~2000], 权限位控制可达8T,若需要请申请开通相关权限。
        - **SourceId** (str) - (Required) 升级目标UDisk ID
        - **UDataArkMode** (str) - (Required) 是否打开数据方舟, 打开"Yes",关闭"No", 默认关闭
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **DiskType** (str) - 磁盘类型，SSDDataDisk:ssd数据盘,DataDisk:普通数据盘,SystemDisk:普通系统盘,SSDSystemDisk:ssd系统盘。默认为DataDisk
        
        **Response**

        - **Price** (float) - 价格
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDiskUpgradePriceRequestSchema().dumps(d)
        resp = self.invoke("DescribeUDiskUpgradePrice", d, **kwargs)
        return apis.DescribeUDiskUpgradePriceResponseSchema().loads(resp)

    def detach_udisk(self, req=None, **kwargs):
        """ DetachUDisk - 卸载某个已经挂载在指定UHost实例上的UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDiskId** (str) - (Required) 需要卸载的UDisk实例ID
        - **UHostId** (str) - (Required) UHost实例ID
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **UHostId** (str) - 卸载的UHost实例ID
        - **UDiskId** (str) - 卸载的UDisk实例ID
        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DetachUDiskRequestSchema().dumps(d)
        resp = self.invoke("DetachUDisk", d, **kwargs)
        return apis.DetachUDiskResponseSchema().loads(resp)

    def rename_udisk(self, req=None, **kwargs):
        """ RenameUDisk - 重命名UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDiskId** (str) - (Required) 重命名的UDisk的Id
        - **UDiskName** (str) - (Required) 重命名UDisk的name
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RenameUDiskRequestSchema().dumps(d)
        resp = self.invoke("RenameUDisk", d, **kwargs)
        return apis.RenameUDiskResponseSchema().loads(resp)

    def resize_udisk(self, req=None, **kwargs):
        """ ResizeUDisk - 调整UDisk容量

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Size** (int) - (Required) 调整后大小, 单位:GB, 范围[1~2000],权限位控制可达8000,若需要请申请开通相关权限。
        - **UDiskId** (str) - (Required) UDisk Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **CouponId** (str) - 使用的代金券id
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ResizeUDiskRequestSchema().dumps(d)
        resp = self.invoke("ResizeUDisk", d, **kwargs)
        return apis.ResizeUDiskResponseSchema().loads(resp)

    def restore_udisk(self, req=None, **kwargs):
        """ RestoreUDisk - 从备份恢复数据至UDisk

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDiskId** (str) - (Required) 需要恢复的盘id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **SnapshotId** (str) - 从指定的快照恢复
        - **SnapshotTime** (int) - 指定从方舟恢复的备份时间点
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.RestoreUDiskRequestSchema().dumps(d)
        resp = self.invoke("RestoreUDisk", d, **kwargs)
        return apis.RestoreUDiskResponseSchema().loads(resp)

    def set_udisk__udataark_mode(self, req=None, **kwargs):
        """ SetUDiskUDataArkMode - 设置UDisk数据方舟的状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDataArkMode** (str) - (Required) 是否开启数据方舟，开启:"Yes", 不支持:"No"
        - **UDiskId** (str) - (Required) 需要设置数据方舟的UDisk的Id
        - **Zone** (str) - (Required) 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        
        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.SetUDiskUDataArkModeRequestSchema().dumps(d)
        resp = self.invoke("SetUDiskUDataArkMode", d, **kwargs)
        return apis.SetUDiskUDataArkModeResponseSchema().loads(resp)
