from rest_framework import serializers
from .models import Teknik, Computer, Elit


class TeknikSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teknik
        fields = ["id", "haid", "tanggal awal haid", "hal waktu haid"]
            class meta:
                model = teknik 
                fields = ["darah yang keluar diwaktu sehat"]
class ComputerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ["id", "haid", "tanggal awal haid", "hal waktu haid"]
            class meta:
            model = teknik 
            fields = ["tentukan tanggal"]
class ElitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Elit
        fields = ["id", "haid", "tanggal awal haid", "hal waktu haid"]
            class meta:
                model = elit 
                fields = ["berbuat baik, perbanyak sedekah, perbanyak dzikir"]