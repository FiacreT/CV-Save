$('.selectpicker').selectpicker();


function displayPanel(id){
    /*
    var education = document.getElementById("education");
    var skills = document.getElementById("skills");
    var work = document.getElementById("work");
    var research = document.getElementById("research");
    var extra = document.getElementById("extra");
    var moocs = document.getElementById("moocs");
    
    
    $('#'+id).click(function(){
        if($(this).prop("checked") == true){
            //alert("Checkbox is checked.");
            $('#'+id+'-card').fadeIn('slow');
        }
        else if($(this).prop("checked") == false){
            //alert("Checkbox is unchecked.");
            $('#'+id+'-card').fadeOut('slow');
            
        }
    });*/

        

        

            if($('#'+id).prop("checked") == true){
                //alert("Checkbox is checked.");
                $('#'+id+'-card').fadeIn('slow');
            }
            else if($('#'+id).prop("checked") == false){
                //alert("Checkbox is unchecked.");
                $('#'+id+'-card').fadeOut('slow');
                
            }

        
    
        
    
}


