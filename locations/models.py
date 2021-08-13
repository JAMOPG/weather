from django.db import models


class Location(models.Model):
    class Meta:
        verbose_name = 'Localizaçao'
        verbose_name_plural = 'Localizações'
        # unique_together = ('city', 'longitude', 'latitude')
        
           
    city = models.CharField(max_length=150, 
                            verbose_name='Cidade')
    state = models.CharField(max_length=5, 
                             null=True,
                             blank=True,
                             verbose_name='Estado')
    country = models.CharField(max_length=3,
                               verbose_name='País', 
                               null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    
    def __str__(self):
        return str(self.city) + ' - ' + str(self.country) 
                                 



# class Country(models.Model):
#     class Meta:
#         verbose_name = 'País'
#         verbose_name_plural = 'Países'
        
#     name = models.CharField(max_length=70, unique=True)
    
#     initials = models.CharField(max_length=5)
    
#     data_edit = models.DateTimeField(auto_now=True)

#     date_joined = models.DateTimeField('Data entry',
#                                        auto_now_add=True)

#     is_active = models.BooleanField(default=True,
#                                     verbose_name='Ativo')


#     def __str__(self):
#         return str(self.name) + ' - ' + str(self.initials)

        
# class State(models.Model):
#     class Meta:
#         verbose_name = 'Estado'
#         verbose_name_plural = 'Estados'
        
#     name = models.CharField(max_length=60, db_index=True)
    
#     initials = models.CharField(max_length=2)
    
#     country = models.ForeignKey(Country, on_delete=models.CASCADE())
    
#     data_edit = models.DateTimeField(auto_now=True)

#     date_joined = models.DateTimeField('Data entry',
#                                        auto_now_add=True)

#     is_active = models.BooleanField(default=True,
#                                     verbose_name='Ativo')


#     def __str__(self):
#         return str(self.name) + ' - ' + str(self.initials)


# class City(models.Model):
#     class Meta:
#         verbose_name = "Cidade"
#         verbose_name_plural = "Cidades"
#         unique_togheter = ('name', 'state')
        
#     name = models.CharField(max_length=75,
#                             db_index=True)
    
#     state =  models.ForeignKey(State, on_delete=models.CASCADE()) 
    
#     data_edit = models.DateTimeField(auto_now=True)

#     date_joined = models.DateTimeField('Data entry',
#                                        auto_now_add=True)

#     is_active = models.BooleanField(default=True,
#                                     verbose_name='Ativo')


#     def __str__(self):
#         return str(self.name) + ' - ' + str(self.state.initials) + ' - ' + + str(self.state.country.initials) 