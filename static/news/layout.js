$( document ).ready(function() {

	function listNews(){
		// load news list
		$.ajax({
			url: '/news/list/',
			type: 'post',
			data: {
				action: 'action',
			},
			success: function(xhr) {
				$("#main-container").html(xhr);
				$(".username").val(xhr.username)
				$(".more-detail").click(function(){
					article_id = $(this).parent().parent().attr("data-id");
					window.location.href = '/news/' + article_id;
				})
			},
			error: function(xhr) {
				if (xhr.status == 403) {
					notify('error', xhr.responseText);
				}
			}
		})		
	}

	listNews();

	$(".feng-menu").click(function(){
		$('.demo.sidebar').sidebar('toggle');
	});

	$("#home").click(function(){
		listNews();
		$('.demo.sidebar').sidebar('toggle');
    	});

	$('.ui.dropdown').dropdown();
});