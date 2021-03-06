from typing import Any, Dict

from app.app import db

Model: Any = db.Model


class Camera(Model):
    __tablename__ = 'cameras'

    Name = db.Column(db.String(10), unique=True)
    images = db.relationship('Image', backref='camera', lazy=True)

    @classmethod
    def from_dict(cls, camera_dict: Dict[str, Any]) -> 'Camera':
        return cls(
            Name=camera_dict['Name']
        )

    def to_dict(self) -> Dict[str, Any]:
        to_dict = super().to_dict()
        to_dict.update(
            {
                'Name': self.Name
            }
        )
        return to_dict

    def update_from_dict(self, camera_dict: Dict[str, Any]) -> None:
        super().update_from_dict(camera_dict)
        if 'Name' in camera_dict:
            self.Name = camera_dict['Name']


class ProductType(Model):
    __tablename__ = 'product_types'

    Name = db.Column(db.String(4), unique=True)
    images = db.relationship('Image', backref='product_type', lazy=True)

    @classmethod
    def from_dict(cls, type_dict: Dict[str, Any]) -> 'ProductType':
        return cls(
            Name=type_dict['Name']
        )

    def to_dict(self) -> Dict[str, Any]:
        to_dict = super().to_dict()
        to_dict.update(
            {
                'Name': self.Name
            }
        )
        return to_dict

    def update_from_dict(self, type_dict: Dict[str, Any]) -> None:
        super().update_from_dict(type_dict)
        if 'Name' in type_dict:
            self.Name = type_dict['Name']


class Image(Model):
    __tablename__ = 'images'

    Name = db.Column(db.String(31), unique=True)
    URL = db.Column(db.Text)
    Sol = db.Column(db.Integer, nullable=False)
    DetatchedLabel = db.Column(db.Boolean)
    CameraID = db.Column(
        db.Integer,
        db.ForeignKey('cameras.ID'),
        nullable=False,
    )
    ProductTypeID = db.Column(
        db.Integer,
        db.ForeignKey('product_types.ID'),
        nullable=False,
    )

    @classmethod
    def from_dict(cls, image_dict: Dict[str, Any]) -> 'Image':
        return cls(
            Name=str(image_dict['Name']),
            URL=str(image_dict['URL']),
            Sol=int(image_dict['Sol']),
            DetatchedLabel=bool(image_dict['DetatchedLabel']),
            CameraID=int(image_dict['CameraID']),
            ProductTypeID=int(image_dict['ProductTypeID']),
        )

    def to_dict(self) -> Dict[str, Any]:
        to_dict = super().to_dict()
        to_dict.update(
            {
                'Name': self.Name,
                'URL': self.URL,
                'Sol': self.Sol,
                'DetatchedLabel': self.DetatchedLabel,
                'CameraID': self.CameraID,
                'camera': self.camera.to_dict(),
                'ProductTypeID': self.ProductTypeID,
                'product_type': self.product_type.to_dict(),
            }
        )
        return to_dict

    def update_from_dict(self, image_dict: Dict[str, Any]) -> None:
        super().update_from_dict(image_dict)
        if 'Name' in image_dict:
            self.Name = image_dict['Name']
        if 'URL' in image_dict:
            self.URL = image_dict['URL']
        if 'Sol' in image_dict:
            self.Sol = image_dict['Sol']
        if 'DetatchedLabel' in image_dict:
            self.DetatchedLabel = image_dict['DetatchedLabel']
        if 'CameraID' in image_dict:
            self.CameraID = image_dict['CameraID']
        if 'ProductTypeID' in image_dict:
            self.ProductTypeID = image_dict['ProductTypeID']
