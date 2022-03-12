console.log('hello world')

var el = document.getElementById( "image" );
const imageBox = document.getElementById("image-box")

el.addEventListener('load', ()=> {
    
    console.log('changed')
    
    const el = document.getElementById( "image" );
    console.log(el.src);
    // console.log(document.getElementById( "image" ).src)

    // el.srcObject = 'http://192.168.1.154:8080/media/P6Math026/pdf_img/page_9.jpg';
    const url = el.src;
    imageBox.innerHTML='<img src="${url}" id="image" width="500px">'
    console.log(imageBox.innerHTML)
    new Cropper(document.getElementById( "image" ));
})
    
new Cropper(document.getElementById( "image" ));