from app.models import product_model,order_detail_model,partner_model,\
order_model,shop_model,model,shipping_model, catagory_model, location_model

Product = product_model.Product
Order_Detail = order_detail_model.Order_Detail
Partner = partner_model.Partner
Order = order_model.Order
Shop = shop_model.Shop
Model = model.Model
Shipping = shipping_model.Shipping
Catagory = catagory_model.Catagory
Location = location_model.Location

ProductsSchema = product_model.ProductSchema
Order_DetailSchema = order_detail_model.Order_DetailSchema
PartnerShema = partner_model.PartnerSchema

ShopSchema =shop_model.ShopSchema
OrderSchema = order_model.OrderSchema
ModelSchema = model.ModelSchema
ShippingSchema = shipping_model.ShippingSchema
CatagorySchema = catagory_model.CatagorySchema
LocationShcema = location_model.LocationSchema