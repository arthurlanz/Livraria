from django.db import models
from .categoria import Categoria
from .editora import Editora
from .autor import Autor

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.DecimalField(max_digits=13, decimal_places=0, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros', null=True, blank=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros', null=True, blank=True)
    autores = models.ManyToManyField(Autor, related_name='livros', blank=True)

    def __str__(self):
        categoria_str = self.categoria.nome if self.categoria else 'Sem categoria'
        editora_str = self.editora.nome if self.editora else 'Sem editora'
        autor_str = self.autor.nome if self.autor else 'Sem autor'
        
        return (f"ID: {self.id} - {self.titulo} "
                f"({self.quantidade or 0} disponíveis - R$ {self.preco:.2f} cada) "
                f"- {categoria_str} - {editora_str} - {autor_str}")
