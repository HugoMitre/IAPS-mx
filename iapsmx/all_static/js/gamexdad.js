var add_permission;
var change_version;
var add_vote;
var change_status_validation;
var update_combobox;
var search_table;
var update_dual_listbox;
var build_item_tree;
var build_nestable;
var save_sort;

add_permission = function(url, permission_id, csrfmiddlewaretoken, action, value, id_check){

    toastr.options = {
                closeButton: true,
                progressBar: true,
                showMethod: 'slideDown',
                timeOut: 4000
            };

    value_new = 1 - value;
    id_check = "#" + id_check;

    $.ajax({
        method: "POST",
        url: url,
        data: {
            permission_id: permission_id,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            action: action,
            value: value
        },
        success:function(data) {
            $(id_check).val(value_new+"|"+action+"|"+permission_id);
            toastr.success('Saved Permission', 'Success');
        },
        error:function(data){
            $(id_check).val(value+"|"+action+"|"+permission_id);
            toastr.error('The request was unsuccessful', 'Error');
        }
    })

};

add_vote= function(url, guideline_id, csrfmiddlewaretoken, value){

    toastr.options = {
                closeButton: true,
                progressBar: true,
                showMethod: 'slideDown',
                timeOut: 4000
            };

    value_new = value;

    $.ajax({
        method: "POST",
        url: url,
        data: {
            guideline_id: guideline_id,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            value: value
        },
        success:function(data) {
            $(guideline_id).val(value_new);
        },
        error:function(data){
            $(guideline_id).val(value);
            toastr.error('The request was unsuccessful', 'Error');
        }
    })

};

change_version = function(url, version, token, url_redirect){

    if(confirm('Are you sure?')) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                version: version,
                csrfmiddlewaretoken: token
            },
            success:function() {
                window.location.replace(url_redirect);
            },
            error:function(){
                window.location.replace(url_redirect);
            }
        });

    }

};

change_status_validation= function(url, guideline_element_id, csrfmiddlewaretoken, value) {

    toastr.options = {
                closeButton: true,
                progressBar: true,
                showMethod: 'slideDown',
                timeOut: 4000
            };

    value_new = value;

    $.ajax({
        method: "POST",
        url: url,
        data: {
            guideline_element_id: guideline_element_id,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            value: value
        },
        success:function(data) {
            $(guideline_element_id).val(value_new);
            toastr.success('Saved Status', 'Success');

        },
        error:function(data){
            $(guideline_element_id).val(value);
            toastr.error('The request was unsuccessful', 'Error');
        }

    })

};

update_combobox= function(url, pk, destiny, destiny_pk, csrfmiddlewaretoken ) {

    if(pk=='')
        pk = 0;

    $.ajax({
        dataType: "json",
        url: url,
        data: {
            pk: pk,
            csrfmiddlewaretoken: csrfmiddlewaretoken
        },
        success:function(data) {
            var options = '<option value="">---------</option>';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['name'] + '</option>';
            }
            $(destiny).html(options);
            $(destiny).val(destiny_pk);

        },
        error:function(data){
            var options = '<option value="">---------</option>';
            $(destiny).html(options);
            $(destiny).val(destiny_pk);
        }

    })

};

update_dual_listbox = function(url, pk, destiny, destiny_pk, csrfmiddlewaretoken ) {

    if(pk=='')
        pk = 0;

    //Obtienes elementos seleccionados
    var selected_elements = [];
    $("select[name='elements[]_myhelper2'] option").each(function(){
        selected_elements.push(parseInt(this.value));
    });

    //Agregar elementos de acuerdo a la categoría
    $.ajax({
        dataType: "json",
        url: url,
        data: {
            pk: pk,
            csrfmiddlewaretoken: csrfmiddlewaretoken
        },
        success:function(data) {

            for (var i = 0; i < data.length; i++) {
                //Compruebas si el elemento a agregar ya esta seleccionado
                if (selected_elements.indexOf(data[i].pk) == -1 ) {
                    $(destiny).append('<option value="' + data[i].pk + '">' + data[i].fields['name'] + '</option>');
                }
            }

             $(destiny).bootstrapDualListbox('refresh', true);

        },
        error:function(data){
            toastr.error('The request was unsuccessful', 'Error');
        }
    });

    //Eliminas opciones que no esten seleccionadas sin revisar los nuevos elementos
    $("#elements option").each(function(){
        if (selected_elements.indexOf(parseInt(this.value)) == -1 ){
            $(this).remove();
        }
        $(destiny).bootstrapDualListbox('refresh', true);
    });

};

search_table = function (inputVal)
{
    var table = $('#my-projects');
    table.find('tr').each(function(index, row)
    {
        var all_cells = $(row).find('td');
        if(all_cells.length > 0)
        {
            var found = false;
            all_cells.each(function(index, td)
            {
                var reg_exp = new RegExp(inputVal, 'i');
                if(reg_exp.test($(td).text()))
                {
                    found = true;
                    return false;
                }
            });
            if(found == true)$(row).show();else $(row).hide();
        }
    });
};

build_item_tree = function (item, open) {

    var node_open = "";
    if (open)
        node_open = "class=\"jstree-open\"";

    var latest_node = "";
    if (item.latest_node)
        latest_node = "data-jstree='{\"type\":\"latest\"}'";

    var html = "<li " + node_open + " " + latest_node + " id='" + item.id + "'>" + item.name;

    if (item.children) {

        html += "<ul>";
        $.each(item.children, function (index, sub) {
            html += build_item_tree(sub, open);
        });
        html += "</ul>";

    }

    html += "</li>";

    return html;
};

build_nestable = function (item){
    var html = "<li class='dd-item' data-id='" + item.id + "'>";
    html += "<div class='dd-handle'>" + item.name + "</div>";


    if (item.children) {

        html += "<ol class='dd-list'>";
        $.each(item.children, function (index, sub) {
            html += build_nestable(sub);
        });
        html += "</ol>";

    }

    html += "</li>";

    return html;
};

save_sort = function(url, json_elements, csrfmiddlewaretoken){

    toastr.options = {
                closeButton: true,
                progressBar: true,
                showMethod: 'slideDown',
                timeOut: 4000
            };

    $.ajax({
        dataType: 'text',
        method: "POST",
        url: url,
        data: {
            json_elements: JSON.stringify(json_elements),
            csrfmiddlewaretoken: csrfmiddlewaretoken
        },
        success:function(data) {
            toastr.success('Flow Saved', 'Success');
        },
        error:function(data){
            toastr.error('The request was unsuccessful', 'Error');
        }
    })

};