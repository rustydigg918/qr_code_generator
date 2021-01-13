import qrcode
import qrcode.image.svg as svg

factory = svg.SvgPathImage
svg_img = qrcode.make("hello world...", image_factory=factory)
svg_img.save("myqr.svg")