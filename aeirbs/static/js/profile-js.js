$(document).ready(function(){
    //SIDENAV
    $('#logo-AEIRBS').show();
    $('#logo').hide();

    $('#dashboard').show();
    $('#dashboard-logo').hide();

    $('#masterlist').show();
    $('#masterlist-logo').hide();

    $('#reports').show();
    $('#reports-logo').hide();

    $('#audit').show();
    $('#audit-logo').hide();

    $('#incident').show();
    $('#incident-logo').hide();

    $('#summary').show();
    $('#summary-logo').hide();

    $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
      if($('#sidebar').hasClass('active')){
        $('#logo-AEIRBS').hide();
        $('#logo').show();

        $('#dashboard').hide();
        $('#dashboard-logo').show();

        $('#masterlist').hide();
        $('#masterlist-logo').show();

        $('#reports').hide();
        $('#reports-logo').show();

        $('#audit').hide();
        $('#audit-logo').show();

        $('#incident').hide();
        $('#incident-logo').show();

        $('#summary').hide();
        $('#summary-logo').show();
      }
      else{
        $('#logo-AEIRBS').show();
        $('#logo').hide();

        $('#dashboard').show();
        $('#dashboard-logo').hide();

        $('#masterlist').show();
        $('#masterlist-logo').hide();

        $('#reports').show();
        $('#reports-logo').hide();

        $('#audit').show();
        $('#audit-logo').hide();

        $('#incident').show();
        $('#incident-logo').hide();

        $('#summary').show();
        $('#summary-logo').hide();
      }
    });

    $("#addAdminForm").hide();
    $("#addAdminLabel").hide();

    $("#addAdminButton" ).click(function() {
      $("#addAdminForm").show();
      $("#addAdminLabel").show();
      $("#masterlistLabel").hide();
      $("#addAdminButton").hide();
      $("#masterlistTable").hide();
      $("#searchAdmin").hide();
      $("#sortMasterlist").hide();
      $("#userDetails").hide();
      $("#masterlistPagination").hide();
      $(".left-padding").width("100%");
      $("#userContainer").css("padding","0 25px 25px 25px");
    });

    /*
    $("#submitAdmin" ).click(function() {
    $("#addAdminForm").hide();
    $("#addAdminLabel").hide();
    $("#masterlistLabel").show();
    $("#addAdminButton").show();
    $("#masterlistTable").show();
    $("#searchAdmin").show();
    $("#sortMasterlist").show();
    $("#userDetails").show();
    $("#users").width("65%");
    $("#userContainer").css("padding","0 12.5px 25px 25px;");
  });

  */

  $("#cancel-addAdmin" ).click(function() {
    $("#addAdminForm").hide();
    $("#addAdminLabel").hide();
    $("#masterlistLabel").show();
    $("#addAdminButton").show();
    $("#masterlistTable").show();
    $("#searchAdmin").show();
    $("#sortMasterlist").show();
    $("#userDetails").hide();
    $("#masterlistPagination").show();
    $(".left-padding").width("100%");
  });


  //Add Image
  $(".imgAdd").click(function(){
    $(this).closest(".row").find('.imgAdd').before('<div class="col-sm-2 imgUp"><div class="imagePreview"></div><label class="btn btn-primary">Upload<input type="file" class="uploadFile img" value="Upload Photo" style="width:0px;height:0px;overflow:hidden;"></label><i class="fa fa-times del"></i></div>');
  });
  $(document).on("click", "i.del" , function() {
    $(this).parent().remove();
  });
  $(function() {
    $(document).on("change",".uploadFile", function()
    {
      var uploadFile = $(this);
      var files = !!this.files ? this.files : [];
      if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support

      if (/^image/.test( files[0].type)){ // only image file
        var reader = new FileReader(); // instance of the FileReader
        reader.readAsDataURL(files[0]); // read the local file

        reader.onloadend = function(){ // set image data as background of div
          //alert(uploadFile.closest(".upimage").find('.imagePreview').length);
          uploadFile.closest(".imgUp").find('.imagePreview').css("background-image", "url("+this.result+")");
        }
      }
    });
  });

  $(".table-row").click(function() {
    $(".left-padding").width("65%");
    $("#userContainer").css("padding", "0 12.5px 25px 25px");
    $("#userDetails").show();
  });

  $("#saveAdmin").hide();
  $("#adminForm").hide();

  //Edit Admin Details
  $("#editAdmin").click(function() {
    $("#adminDetails").hide();
    $("#editAdmin").hide();
    $("#adminForm").show();
    $("#saveAdmin").show();
  });

  //Save Admin Details
  $("#saveAdmin").click(function() {
    $("#adminDetails").show();
    $("#editAdmin").show();
    $("#adminForm").hide();
    $("#saveAdmin").hide();
  });

  //Close Admin Details
  $("#closeAdmin").click(function() {
    $(".left-padding").width("100%");
    $("#userContainer").css("padding", "0 25px 25px 25px");
    $("#userDetails").hide();
  });
});