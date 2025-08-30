from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from helpers.sql.sqlalchemy_helper import Base


class Closet(Base):
    __tablename__ = "closets"
    # Elements
    closet_id = Column(Integer, primary_key=True, autoincrement=True)
    closet_location = Column(Text)
    comments = Column(Text)
    # Relationships
    closet_product = relationship("ClosetProduct", back_populates="closets")


class ClosetProduct(Base):
    __tablename__ = "closet_products"
    # Elements
    closet_product_id = Column(Integer, primary_key=True, autoincrement=True)
    barcode = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String)  # rova Text vs String?
    img_url = Column(Text)
    nutrition_info = Column(Text)
    product_price = Column(Float)
    product_qty = Column(Integer)
    purchase_date = Column(DateTime)
    expiration_date = Column(DateTime)
    product_active = Column(Boolean)
    store = Column(String)
    closet_id = Column(Integer, ForeignKey("closets.closet_id"), nullable=False)
    # Relationships
    closets = relationship("Closet", back_populates="closet_product")
