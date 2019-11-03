function imgUp(args){
     this.filenum = args.filenum;
     this.filename = args.filename;
     this.createitem = function(num = this.filenum) {
        $('#img-box').width(this.filenum*200)
         for (var i = 0; i < num; i++) {
             var item = $('<div class="item"></div>')
             var iteminput = $('<input type="file" name="' + this.filename + '">')
             var itemimg = $('<img src="/static/myadmin/assets/ImgUpRead/a7.png" alt="">')
             item.append(itemimg)
             item.append(iteminput)
             $('#img-box').append(item)
             // 绑定事件
             this.bindchange(iteminput)
             this.bingclick(itemimg)
         }

     };
     this.bindchange = function(obj) {
         obj.change(function() {
             var file = this.files[0]
             var reader = new FileReader();
             reader.readAsDataURL(file);
             reader.onload = function(e) {
                 obj.parent().css('background-image', 'url(' + this.result + ')')
                 obj.hide()
             }
             obj.parent().hover(function() {
                 $(this).find('img').show()
             }, function() {
                 $(this).find('img').hide()
             })
         })


     };
     this.bingclick = function(obj) {
        var $this = this
         obj.click(function() {
             console.log(11)
             obj.parents('.item').remove()
             $this.createitem(1)
         })
     };

 }
