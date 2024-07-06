from rest_framework import serializers
from .models import Teknik, Computer, Elit


class TeknikSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teknik
        fields = ["id", "haid", "tanggal awal haid", "hal waktu haid"]

class ComputerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ["id", "haid", "tanggal awal haid", "hal waktu haid"]

class ElitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Elit
        fields = ["id", "haid", "tanggal awal haid", "hal waktu haid"]
