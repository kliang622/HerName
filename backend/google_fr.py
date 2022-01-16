from crop import Crop
import uuid
from compare import compareImages
from os import listdir


#export GOOGLE_APPLICATION_CREDENTIALS="/home/natem135/Downloads/rosehack2022-f178de763729.json"

def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        # print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        # print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        # print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = ([(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices])
        folder = uuid.uuid4().hex[1:15]
        img = Crop(vertices[0][0], vertices[0][1], vertices[1][0], vertices[1][1], vertices[2][0], vertices[2][1], vertices[3][0], vertices[3][1], path, f"../tmp/{folder}.png")
        img.generate_crop()
        min = 101
        min_str = ""
        for filename in listdir('images/'):
            try:
                val = compareImages(f"../tmp/{folder}.png", f"images/{filename}")
                if val < min:
                    min_str = filename
                    min = val
                print(f"{val}:{filename}")
            except:
                print(f"{filename} broke the thing")
        print(f'{path} is most similar to:')
        print(min_str)
        return min_str

        
    

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))