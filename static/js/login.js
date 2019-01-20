$(function(){

	//用户名匹配
	var isTurel1 = false;
	$('input.login_style_txt1_name').blur(function(){
		 var lreg1 = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9_\.\-]+\.[a-zA-Z]+$/;
		 var loginName= $('.login_style_txt1_name').val();
		 isTurel1 = lreg1.test(loginName);
	     if(!loginName){
	     	$('.flase_lable1').show().siblings('.flase_lable11').hide();
	     }else{
	     	$('.flase_lable1').hide(); 
	     	if(isTurel1){
	     		$('.true_lable1').show().siblings('.flase_lable11').hide();
	        	$(this).css('border','1px solid #C9C9C9');
	     	}else{
	     		$('.true_lable1').hide().siblings('.flase_lable11').show();
	            $(this).css('border','1px solid #e50065');
	     	}
	     }
	});
	
	//密码匹配
	var isTure2 = false;
	$('input.login_style_txt1_pwd').blur(function(){
		var loginPwd= $('.login_style_txt1_pwd').val();
		if(!loginPwd){
			$('.flase_lable2').show();
		}else{
			$('.flase_lable2').hide();
			isTure2 = true;
		}
	})
	
	//判断是否存在该用户(匹配用户名和密码是否都一致)
	$("#txtLoginSub").click(function(){
		if(isTurel1 && isTure2){
			$('.login_stylebox').submit();
		}
	})
	
})
