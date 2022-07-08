# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CoreDocument(models.Model):
    title = models.CharField(max_length=200)
    uploadedfile = models.CharField(db_column='uploadedFile', max_length=100)  # Field name made lowercase.
    datetimeofupload = models.DateTimeField(db_column='dateTimeOfUpload')  # Field name made lowercase.
    texto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Core_document'


class AccountEmailaddress(models.Model):
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AccountsPerfil(models.Model):
    nome_completo = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    curso = models.CharField(max_length=10, blank=True, null=True)
    usuario = models.OneToOneField('AuthUser', models.DO_NOTHING)
    foto = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accounts_perfil'


class AppUpload(models.Model):
    title = models.CharField(max_length=50)
    upload = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_upload'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuxilioAuxilio(models.Model):
    file = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    criado_por = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    publicada = models.BooleanField()
    titulo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auxilio_auxilio'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstagioEstagio(models.Model):
    file = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_por = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    postar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'estagio_estagio'


class FileUploadFile(models.Model):
    file = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=20, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    equipe = models.TextField(blank=True, null=True)
    turma = models.CharField(max_length=20, blank=True, null=True)
    curso = models.CharField(max_length=20, blank=True, null=True)
    orientador = models.CharField(max_length=20, blank=True, null=True)
    criado_por = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    postar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'file_upload_file'


class InformesPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)
    postar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'informes_post'


class PerfilCampus(models.Model):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cargo = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    nome_completo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil_campus'


class PessoasPessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    texto = models.TextField(blank=True, null=True)
    escolaridade = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas_pessoa'


class RegrasReceita(models.Model):
    categoria = models.CharField(max_length=100)
    publicada = models.BooleanField()
    criado_por = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    date_foto = models.DateTimeField()
    descricao = models.TextField()
    lugar = models.TextField()
    nome_foto = models.CharField(max_length=200)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'regras_receita'


class ServidorPerfil(models.Model):
    nome_completo = models.CharField(max_length=50, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    telefone = models.CharField(max_length=16, blank=True, null=True)
    usuario = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servidor_perfil'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
