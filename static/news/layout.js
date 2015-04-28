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
				$(".more-detail").click(function(){
					article_id = $(this).parent().parent().attr("data-id");
					$.ajax({
						url: '/news/' + article_id + '/',
						type: 'post',
						success: function(xhr) {
							$("#main-container").html(xhr);

							$(".delete-article").click(function(){
								$.ajax({
									url: '/news/delete/',
									type: 'post',
									data: {
										article_id: article_id,
									},
									success: function(xhr) {
										listNews();
									},
									error: function(xhr) {
										if (xhr.status == 403) {
											notify('error', xhr.responseText);
										}
									}
								})
							});			

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

				$("#extract-url-btn").click(function(){
					$('.ui.modal.extract_url').modal('show');
					
					$("#extract-url-submit-btn").click(function(){
						//tinyMCE.activeEditor.setContent($('#extract-url').val());
						url = $('#extract-url').val();
						$.ajax({
							url: '/news/extract_url/',
							type: 'post',
							data: {
								url: url,
								action: 'action',
							},
							success: function(xhr) {
								console.log(xhr.content);
								$('.title').val(xhr.title);
								tinyMCE.activeEditor.setContent(xhr.content);
							},
							error: function(xhr) {
								if (xhr.status == 403) {
									notify('error', xhr.responseText);
								}
							}
						})			
					});
				});


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