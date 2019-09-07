from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


"""
"""
class MapTypes:    
    UNDEFINED = 'UN'
    PATHMAP = 'PM'
    ICONMAP = 'IM'
    SMALLPOLYGONMAP = 'SP'
    SCATTERPLOTMAP = "SM"
    TEXT = "TX"
    CHLOROPLETHMAP = 'CM'
    DEFAULT = UNDEFINED


    Choices = (
        (UNDEFINED, 'UN'),
        (PATHMAP, 'Path Map'),
        (ICONMAP, 'Icon Map'),
        (SMALLPOLYGONMAP, 'Small Polygon Map'),
        (SCATTERPLOTMAP, 'ScatterPlot Map'),
        (TEXT, 'Text'),
        (CHLOROPLETHMAP, 'Choropleth Map'),
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return MapTypes.UNDEFINED


"""
"""
class Ratings:
    UNDEFINED = "UN"
    OPEN = "OP"
    CURATED = "CU"
    BLOCKED = "BL"
    DEFAULT = UNDEFINED

    Choices = (
        (UNDEFINED, "UN"),
        (OPEN, 'Open'),
        (CURATED, 'Curated'),
        (BLOCKED, 'Blocked'),
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return Ratings.UNDEFINED    

"""
"""
class CurationFlags:
    UNDEFINED = "UN"
    CIVIC_CURATED = "CC"
    CIVIC_ENDORSED = "CE"
    CONTRIBUTOR_ASSEMBLED = "CA"
    USER_ASSEMBLED = "UA"
    DEFAULT = UNDEFINED

    Choices =  (
        (UNDEFINED, "UN"),
        (CIVIC_CURATED, 'Civic Curated'),
        (CIVIC_ENDORSED, 'Civic Endorsed'),
        (CONTRIBUTOR_ASSEMBLED, 'Contributor Assembled'),
        (USER_ASSEMBLED, 'User Assembled'),
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k    
        return CurationFlags.UNDEFINED    


"""
"""
class AggregationFlags:
    UNDEFINED = "UN"
    AGGREGATABLE = "AG"
    AGGREGATE_BY = "AB"
    PRE_AGGREGATED = "PA"
    NONE = "NO"
    DEFAULT = NONE

    Choices = (
        (UNDEFINED, "UN"),
        (AGGREGATABLE, 'Aggregatable'),
        (AGGREGATE_BY, 'Aggregate By'),
        (PRE_AGGREGATED, 'Pre-Aggregated'),
        (NONE, 'None')
    )

    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return AggregationFlags.UNDEFINED


"""
"""
class VisualizationTypes:
    UNDEFINED = "UN"
    DONUT_CHART = "DC"
    STACKED_BARS = "SB"
    TEXT = "TE"    
    DEFAULT = UNDEFINED

    Choices = (
        (UNDEFINED, "UN"),
        (DONUT_CHART, 'Donut Chart'),
        (STACKED_BARS, 'Stacked Bars'),
        (TEXT, 'Text'),       
    )

    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return VisualizationTypes.UNDEFINED

"""
"""
class FormatTypes:
    UNDEFINED = "UN"
    SENTENCE_CASE = "SC"
    TITLE_CASE = "TC"
    NUMERIC = "NU"
    NUMERIC_SHORT = "NS"
    DECIMAL = "DE"
    PERCENT = "PE"
    DOLLARS = "DO"
    YEAR = "YE"
    MONTH_YEAR = "MY"
    DEFAULT = UNDEFINED

    Choices = (
        (UNDEFINED, "UN"),
        (SENTENCE_CASE, 'Sentence Case'),
        (TITLE_CASE, 'Title Case'),
        (NUMERIC, 'Numeric'),
        (NUMERIC_SHORT, 'Numeric Short'),
        (DECIMAL, 'Decimal'),
        (PERCENT, 'Percent'),
        (DOLLARS, 'Dollars'),
        (YEAR, 'Year'),
        (MONTH_YEAR, 'Month Year'),       
    )

    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return FormatTypes.UNDEFINED


"""
"""
class DateGranularities:
    UNDEFINED = "UN"
    MONTHS = "MO"
    YEARS = "YR"
    DECADES = "DE"    
    DEFAULT = UNDEFINED

    Choices = (
        (UNDEFINED, "UN"),
        (MONTHS, 'Months'),
        (YEARS, 'Years'),
        (DECADES, 'Decades'),        
    )

    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return DateGranularities.UNDEFINED      


        
class IconMapping(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    mask = models.BooleanField()

class ColorArea(models.Model):
    color = models.CharField(max_length=50)
    area = models.CharField(max_length=50)

"""
"""

class Map(models.Model):
    mapType = models.CharField(max_length=2, choices=MapTypes.Choices, default=MapTypes.DEFAULT)
    civicColor = models.CharField(max_length=50)
    opacity = models.DecimalField(max_digits=5, decimal_places=2)
    scaleType = models.ForeignKey(ColorArea, on_delete=models.CASCADE, related_name='scaleType')
    fieldName = models.ForeignKey(ColorArea, on_delete=models.CASCADE, related_name='fieldName')
    dataRange = ArrayField(ArrayField(models.CharField(max_length=50)))
    colorRange = ArrayField(ArrayField(models.IntegerField()))
    radius = models.IntegerField()
    radiusScale = models.IntegerField()
    lineWidth = models.IntegerField()
    squareSize = models.IntegerField()
    iconSize = models.IntegerField()
    iconAtlas = models.CharField(max_length=50)
    #iconMapping = models.ForeignKey(IconMapping, on_delete=models.CASCADE)

"""
"""

class DashboardEntityObject(models.Model):
    visualization_type = models.CharField(max_length=2, choices=VisualizationTypes.Choices, default=VisualizationTypes.DEFAULT)
    field_name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    format = models.CharField(max_length=2, choices=FormatTypes.Choices, default=FormatTypes.DEFAULT)

"""
"""

class Dashboard(models.Model):
    primary = models.ForeignKey(DashboardEntityObject, on_delete=models.CASCADE, related_name='primary')
    secondary = models.ForeignKey(DashboardEntityObject, on_delete=models.CASCADE, related_name='secondary')

"""
"""

class TooltipEntityObject(models.Model):
    field_name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    format = models.CharField(max_length=2, choices=FormatTypes.Choices, default=FormatTypes.DEFAULT)

"""
"""

class Tooltip(models.Model):
    primary = models.ForeignKey(TooltipEntityObject, on_delete=models.CASCADE, related_name='primary')
    secondary = models.ForeignKey(TooltipEntityObject, on_delete=models.CASCADE, related_name='secondary')

"""
"""

class Dates(models.Model):
    dateFieldName = models.CharField(max_length=50)
    dateGranularity = models.CharField(max_length=2, choices=DateGranularities.Choices, default=DateGranularities.DEFAULT)
    defaultDateFilter = models.CharField(max_length=50)
    minDate = models.CharField(max_length=50)
    maxDate = models.CharField(max_length=50)

"""
"""

class Tag(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

"""
"""

class Visualization(models.Model):
    map =  models.ForeignKey(Map, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='dashboard')
    tooltip = models.ForeignKey(Tooltip, on_delete=models.CASCADE, related_name='tooltip')
    dates = models.ForeignKey(Dates, on_delete=models.CASCADE)
#    1.1.8 visualizations: map
#    1.1.9 visualizations: dashboard
#    1.1.10 visualizations: tooltip
#    1.1.11 visualizations: dates


"""
"""
class Layer(models.Model):
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(auto_now=True)    
    name = models.CharField(max_length=50, unique=True)
    data = models.URLField()
    metadata = models.URLField()
    rating = models.CharField(max_length=2, choices=Ratings.Choices, default=Ratings.DEFAULT)
    visualization = models.ForeignKey(Visualization, on_delete=models.CASCADE)
    creator = models.CharField(max_length=50)
    aggregation = models.CharField(max_length=2, choices=AggregationFlags.Choices, default=AggregationFlags.DEFAULT)    
    tags = models.ManyToManyField(Tag)    
#  1.1 📗 Layer
#    1.1.1 displayName
#    1.1.2 data
#    1.1.3 meta
#    1.1.4 rating
#    1.1.5 association
#    1.1.6 tags
#    1.1.7 aggregationFlag


"""
"""
class Package(models.Model):
    name = models.CharField(max_length=50, unique=True)
    metadata_endpoint = models.URLField()    
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(auto_now=True)   
    contributor = models.CharField(max_length=50, null=True)
    curation = models.CharField(max_length=2, choices=CurationFlags.Choices, default=CurationFlags.DEFAULT)
    layers = models.ManyToManyField(Layer)
    affiliation = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)    
