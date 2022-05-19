from operator import ipow
from django.contrib import admin
from .models import *

admin.site.register((MainCategory,
                        SubCategory,
                            Brand,
                                Product))
