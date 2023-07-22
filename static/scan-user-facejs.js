

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/static/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/static/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('/static/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('/static/models'),
])


function takeFacePhote() {
  console.log('takeFacePhote')
  var faceDetected = window.open('/face_detect/', 'Take Face picture', 'width=720,height=560');

}

window.addEventListener('message', event => {
  if (event.origin !== window.location.origin) {
    return;
  }
  if (event.data.type === 'picture') {
    const pictureDataUrl = event.data.dataUrl;
    // Handle the picture data here
    const img = new Image();
    img.src = pictureDataUrl;
    img.addEventListener('load', async () => {
      const canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext('2d').drawImage(img, 0, 0, canvas.width, canvas.height);
      canvas.toBlob(async blob => {
        const file = new File([blob], 'picture.png', { type: 'image/png' });
        // Assuming you have a div element with the ID 'picture-preview'
        const previewDiv = document.getElementById('picture-preview');
        // Create a new img element to display the image
        const previewImg = document.createElement('img');

        

        previewImg.src = URL.createObjectURL(file);
        previewDiv.appendChild(previewImg);
      }, 'image/png');
    });
  }
});

