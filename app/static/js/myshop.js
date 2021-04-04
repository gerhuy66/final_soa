let productImageFile;
function openCreateProForm()
{
    $("#createProductFrm").slideDown( "slow", function() {
        // Animation complete.
      });
}

function attachProductImagefile(){
    $("#productImage").click();

}

async function saveProduct(){
    //upload product image to server
    var formData = new FormData();
    var imagefile = document.querySelector('#file');
    formData.append("productImage", productImageFile);
    var rp =await axios.post('uploadProductFile', formData, {
        headers: {
        'Content-Type': 'multipart/form-data'
        }
    })

    //insert db
    var ro = {
        pname:$("#creProTiltle").val,
        p_des:$("#pro_des").val,
        p_price:$("#pro_price").val,
        loc:$("#locs option:selected").val,
        catagory:$("#catas option:selected").val,
        

    };
    await axios.post("/createProduct")
}

function attachProductFilrHandle(event){
    var file = event.target.files[0];
    productImageFile = file;

    var url = URL.createObjectURL(file)
    $("#productPic").css('background-image', 'url(' + url + ')');
    // alert(file.name);
}

function onloadMyshop()
{
    $("#createProductFrm").hide();
}