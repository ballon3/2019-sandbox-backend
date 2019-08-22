# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.gis.db import models


class CommunityGardensV20190122(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    propertyid = models.IntegerField(blank=True, null=True)
    sitename = models.CharField(max_length=50, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    r_value = models.IntegerField(blank=True, null=True)
    plotspergarden = models.IntegerField(blank=True, null=True)
    waitlist = models.IntegerField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_gardens_v2019_01_22'


class ParksV20190129(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    propertyid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parks_v2019_01_29'


class PdxMsa2010CensusBlockGroups(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    tract = models.CharField(max_length=50, blank=True, null=True)
    tract_no = models.FloatField(blank=True, null=True)
    bg = models.CharField(max_length=50, blank=True, null=True)
    trbg = models.CharField(max_length=50, blank=True, null=True)
    fips = models.CharField(max_length=50, blank=True, null=True)
    pop10 = models.IntegerField(blank=True, null=True)
    du10 = models.IntegerField(blank=True, null=True)
    vac10 = models.IntegerField(blank=True, null=True)
    white = models.IntegerField(blank=True, null=True)
    black = models.IntegerField(blank=True, null=True)
    aian = models.IntegerField(blank=True, null=True)
    asian = models.IntegerField(blank=True, null=True)
    nhpi = models.IntegerField(blank=True, null=True)
    other_race = models.IntegerField(blank=True, null=True)
    pop_2_race = models.IntegerField(blank=True, null=True)
    hispanic = models.IntegerField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdx_msa_2010_census_block_groups'


class PdxMsa2010CensusTracts(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    tract = models.CharField(max_length=50, blank=True, null=True)
    tract_no = models.FloatField(blank=True, null=True)
    fips = models.CharField(max_length=50, blank=True, null=True)
    pop10 = models.IntegerField(blank=True, null=True)
    du10 = models.IntegerField(blank=True, null=True)
    vac10 = models.IntegerField(blank=True, null=True)
    white = models.IntegerField(blank=True, null=True)
    black = models.IntegerField(blank=True, null=True)
    aian = models.IntegerField(blank=True, null=True)
    asian = models.IntegerField(blank=True, null=True)
    nhpi = models.IntegerField(blank=True, null=True)
    other_race = models.IntegerField(blank=True, null=True)
    pop_2_race = models.IntegerField(blank=True, null=True)
    hispanic = models.IntegerField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdx_msa_2010_census_tracts'


class PdxMsaNcdb(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geo_fips = models.BigIntegerField(blank=True, null=True)
    geo_state = models.IntegerField(blank=True, null=True)
    geo_county = models.IntegerField(blank=True, null=True)
    geo_tract = models.IntegerField(blank=True, null=True)
    cbsa = models.IntegerField(blank=True, null=True)
    metroname = models.CharField(max_length=50, blank=True, null=True)
    tractcontrol = models.IntegerField(blank=True, null=True)
    tractpopulation2010 = models.IntegerField(blank=True, null=True)
    medinc_90 = models.FloatField(blank=True, null=True)
    medinc_00 = models.FloatField(blank=True, null=True)
    medinc_10 = models.FloatField(blank=True, null=True)
    medinc_17 = models.FloatField(blank=True, null=True)
    medhomeval_90 = models.FloatField(blank=True, null=True)
    medhomeval_00 = models.FloatField(blank=True, null=True)
    medhomeval_10 = models.FloatField(blank=True, null=True)
    medhomeval_17 = models.FloatField(blank=True, null=True)
    medrentval_90 = models.FloatField(blank=True, null=True)
    medrentval_00 = models.FloatField(blank=True, null=True)
    medrentval_10 = models.FloatField(blank=True, null=True)
    medrentval_17 = models.FloatField(blank=True, null=True)
    ownshare_90 = models.FloatField(blank=True, null=True)
    ownshare_00 = models.FloatField(blank=True, null=True)
    ownshare_10 = models.FloatField(blank=True, null=True)
    ownshare_17 = models.FloatField(blank=True, null=True)
    whiteshare_90 = models.FloatField(blank=True, null=True)
    whiteshare_00 = models.FloatField(blank=True, null=True)
    whiteshare_10 = models.FloatField(blank=True, null=True)
    whiteshare_17 = models.FloatField(blank=True, null=True)
    blackshare_90 = models.FloatField(blank=True, null=True)
    blackshare_00 = models.FloatField(blank=True, null=True)
    blackshare_10 = models.FloatField(blank=True, null=True)
    blackshare_17 = models.FloatField(blank=True, null=True)
    hispshare_90 = models.FloatField(blank=True, null=True)
    hispshare_00 = models.FloatField(blank=True, null=True)
    hispshare_10 = models.FloatField(blank=True, null=True)
    hispshare_17 = models.FloatField(blank=True, null=True)
    asothshare_90 = models.FloatField(blank=True, null=True)
    asothshare_00 = models.FloatField(blank=True, null=True)
    asothshare_10 = models.FloatField(blank=True, null=True)
    asothshare_17 = models.FloatField(blank=True, null=True)
    rentcbshare_90 = models.FloatField(blank=True, null=True)
    rentcbshare_00 = models.FloatField(blank=True, null=True)
    rentcbshare_10 = models.FloatField(blank=True, null=True)
    rentcbshare_17 = models.FloatField(blank=True, null=True)
    povrate_90 = models.FloatField(blank=True, null=True)
    povrate_00 = models.FloatField(blank=True, null=True)
    povrate_10 = models.FloatField(blank=True, null=True)
    povrate_17 = models.FloatField(blank=True, null=True)
    bachshare_90 = models.FloatField(blank=True, null=True)
    bachshare_00 = models.FloatField(blank=True, null=True)
    bachshare_10 = models.FloatField(blank=True, null=True)
    bachshare_17 = models.FloatField(blank=True, null=True)
    chrent_9017 = models.FloatField(blank=True, null=True)
    chrent_0017 = models.FloatField(blank=True, null=True)
    chrent_1017 = models.FloatField(blank=True, null=True)
    chinc_9017 = models.FloatField(blank=True, null=True)
    chinc_0017 = models.FloatField(blank=True, null=True)
    chinc_1017 = models.FloatField(blank=True, null=True)
    chhomeval_9017 = models.FloatField(blank=True, null=True)
    chhomeval_0017 = models.FloatField(blank=True, null=True)
    chhomeval_1017 = models.FloatField(blank=True, null=True)
    chbachshare_9017 = models.FloatField(blank=True, null=True)
    chbachshare_0017 = models.FloatField(blank=True, null=True)
    chbachshare_1017 = models.FloatField(blank=True, null=True)
    chwhiteshare_9017 = models.FloatField(blank=True, null=True)
    chwhiteshare_0017 = models.FloatField(blank=True, null=True)
    chwhiteshare_1017 = models.FloatField(blank=True, null=True)
    chblackshare_9017 = models.FloatField(blank=True, null=True)
    chblackshare_0017 = models.FloatField(blank=True, null=True)
    chblackshare_1017 = models.FloatField(blank=True, null=True)
    chhispshare_9017 = models.FloatField(blank=True, null=True)
    chhispshare_0017 = models.FloatField(blank=True, null=True)
    chhispshare_1017 = models.FloatField(blank=True, null=True)
    chasothshare_9017 = models.FloatField(blank=True, null=True)
    chasothshare_0017 = models.FloatField(blank=True, null=True)
    chasothshare_1017 = models.FloatField(blank=True, null=True)
    chownshare_9017 = models.FloatField(blank=True, null=True)
    chownshare_0017 = models.FloatField(blank=True, null=True)
    chownshare_1017 = models.FloatField(blank=True, null=True)
    chpovrate_9017 = models.FloatField(blank=True, null=True)
    chpovrate_0017 = models.FloatField(blank=True, null=True)
    chpovrate_1017 = models.FloatField(blank=True, null=True)
    chrentcbshare_9017 = models.FloatField(blank=True, null=True)
    chrentcbshare_0017 = models.FloatField(blank=True, null=True)
    chrentcbshare_1017 = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdx_msa_ncdb'
