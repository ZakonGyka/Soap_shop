document.addEventListener('DOMContentLoaded', function () {
    var cat_urls = document.querySelectorAll('.categoryUrl')
    cat_urls.forEach(function(linker){
        linker.onclick = function(e){
            var cat_set = {'category':this.text, }
            e.preventDefault();
            $.ajax({
                type:'GET',
                url:'/shop/',
                data:cat_set,
                success: function(response) {
                    window.location.replace(`http://127.0.0.1:8000/shop/?${response['urls']}`)
                },
            })
        }
    })
})

