from django.db import models
import uuid

# Create your models here.

class Region(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        db_table = "region"

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "district"

    def __str__(self) -> str:
        return self.name

class Town(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "town"

    def __str__(self) -> str:
        return self.name
