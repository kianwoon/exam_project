console.log('hello world 3')
var $image = $('#image')
console.log($image)

$image.cropper({
    aspectRatio: 16 / 9,
    crop: function(event) {
        console.log(event.detail.x);
        console.log(event.detail.y);
        console.log(event.detail.width);
        console.log(event.detail.height);
        console.log(event.detail.rotate);
        console.log(event.detail.scaleX);
        console.log(event.detail.scaleY);
    }
});

var cropper = $image.data('cropper');
