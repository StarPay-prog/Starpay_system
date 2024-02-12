from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations: True

    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('Phone Email is required')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active',True)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(email,password,**extra_fields)
        