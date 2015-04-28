$( document ).ready(function() {
	// load news list
	$.ajax({
		url: '/news/list/',
		type: 'post',
		data: {
			action: 'action',
		},
		success: function(xhr) {
			$("#main-container").html(xhr)
		},
		error: function(xhr) {
			if (xhr.status == 403) {
				notify('error', xhr.responseText);
			}
		}
	})	

    	$(".feng-menu").click(function(){
	    	$('.demo.sidebar').sidebar('toggle');
    	});

    	$("#home").click(function(){
		$.ajax({
			url: '/news/list/',
			type: 'post',
			data: {
				action: 'action',
			},
			success: function(xhr) {
				$("#main-container").html(xhr);
			},
			error: function(xhr) {
				if (xhr.status == 403) {
					notify('error', xhr.responseText);
				}
			}
		})
		$('.demo.sidebar').sidebar('toggle');
    	});
    	
    	$('.ui.dropdown').dropdown();
    	
    	$("#add-article-btn").click(function(){
		$.ajax({
			url: '/news/edit/',
			type: 'post',
			data: {
				action: 'action',
			},
			success: function(xhr) {
				$("#main-container").html(xhr);
				// $("#page-title").text("撰写新消息").show();
		                	tinymce.init({
			                   	selector:'textarea'
		                	});
				$("#news-category").hide();
				$("#return").show();
				    	$("#add-article-submit-btn").click(function(){
			    		title = $('.title').val();
			    		author = $('.author').val();
			    		content = tinyMCE.activeEditor.getContent();
					$.ajax({
						url: '/news/add/',
						type: 'post',
						data: {
							title: title,
							author: author,
							content: content,
						},
						success: function(xhr) {

						},
						error: function(xhr) {
							if (xhr.status == 403) {
								notify('error', xhr.responseText);
							}
						}
					})
			    	})
			},
			error: function(xhr) {
				if (xhr.status == 403) {
					notify('error', xhr.responseText);
				}
			}
		})
    	})


});