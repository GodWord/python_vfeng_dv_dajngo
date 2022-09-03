from django.contrib.auth import get_user_model
from django.db import models


class Module(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    module_code = models.CharField(max_length=64, unique=True, verbose_name='模块编码')
    module_value = models.CharField(max_length=64, unique=True, verbose_name='模块值')
    module_url = models.CharField(max_length=128, verbose_name='模块路径')
    module_name = models.CharField(max_length=20, verbose_name='模块名称')
    parent_module = models.ForeignKey('Module', on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name='父级模块')
    meta = models.JSONField(default=dict, null=True, blank=True, verbose_name='路由元数据')
    module_desc = models.TextField(null=True, blank=True, verbose_name='描述')


class Action(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    action_code = models.CharField(max_length=64, unique=True, verbose_name='操作编码')
    action_value = models.CharField(max_length=64, unique=True, verbose_name='操作值')
    action_name = models.CharField(max_length=64, verbose_name='操作名称')


class Permit(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    permit_code = models.CharField(max_length=64, unique=True, verbose_name='权限编码')
    module_code = models.ForeignKey('Module', on_delete=models.CASCADE, verbose_name='模块ID')
    action_code = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name='操作ID')
    permit_value = models.CharField(max_length=64, unique=True, verbose_name='权限值')


class PermitGroup(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    group_code = models.CharField(max_length=64, unique=True, verbose_name='权限组编码')
    group_name = models.CharField(max_length=64, verbose_name='权限组名称')
    permit_value = models.CharField(max_length=5120, default='', verbose_name='权限值')


class RolerPermit(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    role_code = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name='角色代码')
    permit_value = models.CharField(max_length=5120, default='', verbose_name='权限值')


class Role(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    role_code = models.CharField(max_length=64, unique=True, verbose_name='角色编码')
    role_name = models.CharField(max_length=64, verbose_name='角色名称')
    role_desc = models.CharField(max_length=64, verbose_name='角色描述')


class UserPermit(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='ID')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='用户')
    role_codes = models.CharField(max_length=256, verbose_name='角色集合')
    # position_codes = models.CharField(max_length=256, verbose_name='职位集合')
    permit_value = models.CharField(max_length=5120, default='', verbose_name='权限值')
    total_permit_value = models.CharField(max_length=5120, default='', verbose_name='权限值')

# class PositionPermitAbstract(models.Model):
#     id = models.BigAutoField(primary_key=True, verbose_name='ID')
#     position_code = models.ForeignKey('Position', on_delete=models.CASCADE, verbose_name='职位代码')
#     permit_value = models.CharField(max_length=5120, default='', verbose_name='权限值')
#
#     class Meta:
#         abstract = True


# class PositionPermit(PositionPermitAbstract):
#     pass


# class Position(models.Model):
#     id = models.BigAutoField(primary_key=True, verbose_name='ID')
#     position_code = models.CharField(max_length=64, unique=True, verbose_name='职位编码')
#     position_name = models.CharField(max_length=64, verbose_name='职位名称')
#     position_desc = models.CharField(max_length=64, verbose_name='职位描述')
#     dept_id = models.ForeignKey(settings.GUARD_DEPT_MODEL, on_delete=models.CASCADE, verbose_name='部门ID')


# class Department(models.Model):
#     id = models.BigAutoField(primary_key=True, verbose_name='ID')
#     dept_code = models.CharField(max_length=64, unique=True, verbose_name='部门编码')
#     dept_name = models.CharField(max_length=64, verbose_name='部门名称')
#     parent_dept = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True,
#                                     verbose_name='上级部门')
#     position_desc = models.CharField(max_length=64, verbose_name='部门描述')
#     company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='dept', verbose_name='所属公司')


# class Company(models.Model):
#     id = models.BigAutoField(primary_key=True, verbose_name='ID')
#     company_code = models.CharField(max_length=64, unique=True, verbose_name='公司编码')
#     company_name = models.CharField(max_length=64, verbose_name='公司名称')
