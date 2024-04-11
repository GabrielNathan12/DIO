from app.contrib.models import BaseModel
from datetime import datetime
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    categoria = relationship('CategoriaModel', back_populates='atletas', lazy='selectin')
    
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_de_treinamento.pk_id'))
    centro_treinamento = relationship('CentroTreinamentoModel', back_populates='atletas', lazy='selectin')
