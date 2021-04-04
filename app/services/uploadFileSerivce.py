from app import app
import os

def uploadProductFile(file):
    file.save(os.path.join(app.config['PRODUCT_UPLOAD_FOLDER'], file.filename))