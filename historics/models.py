from django.db import models


class Historic(models.Model):
    class Meta:
        verbose_name = "Histórico"
        verbose_name_plural = "Históricos"
        
    user = models.CharField(max_length=50, default='padrão')
    location = models.ForeignKey('locations.Location',
                                 on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.user) + ' - '+ str(self.location.city)
        
