from datetime import datetime   

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Profissional(Base):
    __tablename__ = "profissionais"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    especialidade: Mapped[str] = mapped_column(String(100), nullable=False)

class Paciente(Base):
    __tablename__ = "pacientes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), nullable=False)

class Agendamento(Base):
    __tablename__ = "agendamento"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    fim: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    profissional_id: Mapped[int] = mapped_column(ForeignKey("profissionais.id"), nullable=False)
    paciente_id: Mapped[int] = mapped_column(ForeignKey("pacientes.id"), nullable=False)
    data_hora: Mapped[datetime] = mapped_column(DateTime, nullable=False)