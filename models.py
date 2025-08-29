from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from helpers.sql.setup_database import Base


class Category(Base):
    __tablename__ = "categories"
    # Elements
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False)
    # Relationships
    closet_product = relationship("ClosetProduct", back_populates="categories")


class Store(Base):
    __tablename__ = "stores"
    # Elements
    store_id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String)#rova, nullable=False)
    store_url = Column(Text)
    # Relationships
    closet_product = relationship("ClosetProduct", back_populates="stores")


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
    product_id = Column(Integer)
    product_name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    product_img_url = Column(Text)
    product_nutrition_info = Column(Text)
    product_price = Column(Float)
    product_qty = Column(Integer)
    purchase_date = Column(DateTime)
    expiration_date = Column(DateTime)
    product_active = Column(Boolean)
    store_id = Column(Integer, ForeignKey("stores.store_id"), nullable=False)
    closet_id = Column(Integer, ForeignKey("closets.closet_id"), nullable=False)
    # Relationships
    categories = relationship("Category", back_populates="closet_product")
    stores = relationship("Store", back_populates="closet_product")
    closets = relationship("Closet", back_populates="closet_product")
