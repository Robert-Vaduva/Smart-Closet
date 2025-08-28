from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from helpers.sql.setup_database import Base


class Category(Base):
    __tablename__ = "categories"
    # Elements
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False)
    # Relationships
    product = relationship("Product", back_populates="category")
    nutrition = relationship("Nutrition", back_populates="category")


class Nutrition(Base):
    __tablename__ = "nutrition"
    # Elements
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    type = Column(String, nullable=False)
    # Relationships
    category = relationship("Category", back_populates="nutrition")


class Store(Base):
    __tablename__ = "stores"
    # Elements
    store_id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String, nullable=False)
    store_api_url = Column(Text)
    # Relationships
    product = relationship("Product", back_populates="store")


class Product(Base):
    __tablename__ = "products"
    # Elements
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    product_img_url = Column(Text)
    product_nutrition_info = Column(Text)
    product_price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.store_id"), nullable=False)
    # Relationships
    category = relationship("Category", back_populates="product")
    store = relationship("Store", back_populates="product")
    closet_product = relationship("ClosetProduct", back_populates="product")


class Closet(Base):
    __tablename__ = "closets"
    # Elements
    closet_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    closet_location = Column(Text)
    # Relationships
    closet_product = relationship("ClosetProduct", back_populates="closet")


class ClosetProduct(Base):
    __tablename__ = "closet_products"
    # Elements
    closet_product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    closet_id = Column(Integer, ForeignKey("closets.closet_id"), nullable=False)
    product_qty = Column(Integer, default=0)
    purchase_date = Column(DateTime)
    expiration_date = Column(DateTime)
    product_active = Column(Boolean)
    # Relationships
    closet = relationship("Closet", back_populates="closet_product")
    product = relationship("Product", back_populates="closet_product")
