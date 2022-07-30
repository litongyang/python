

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		


<meta charset="UTF-8">
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<meta http-equiv="Cache-Control" content="no-store"/>
<meta http-equiv="Pragma" content="no-cache"/>
<meta http-equiv="Expires" content="0"/>













<script type="text/javascript">
var MachineLog = {};
MachineLog.clinetIp = '10.180.214.125';
MachineLog.groupId = '123';
MachineLog.workNo = '123';
</script>

<link href="/resource/css/base/FormText.css?v=3161" rel="stylesheet" type="text/css" />
<link href="/resource/css/base/block.css" rel="stylesheet" type="text/css" />
<link href="/resource/css/base/ng35.css" rel="stylesheet" type="text/css" />

<script src="/resource/js/jquery-1.7.1.js" type="text/javascript"></script>
<script src="/resource/scripts/base/system/system.js?v=3161" type="text/javascript"></script>
<script src="/resource/scripts/base/plugins/common.js?v=3161" type="text/javascript"></script>
<script src="/resource/scripts/base/plugins/validate_class.js?v=3161" type="text/javascript"></script>
<script src="/resource/scripts/json2.js" type="text/javascript"></script>
<script src="/resource/scripts/My97DatePicker/WdatePicker.js" type="text/javascript"></script>
<script src="/resource/js/page.js?v=3161" type="text/javascript"></script>
<script src="/resource/js/public.js?v=3161" type="text/javascript"></script>
<script src="/resource/njs/si/core_agile_pack.js?v=3161" type="text/javascript"></script>

<script src="/resource/scripts/base/redialog/rd-config.js"     type="text/javascript"></script>
  <script src="/resource/scripts/base/redialog/redialog.js"></script>
<script type="text/javascript" src="/resource/njs/exportToExcel.js"></script>
<script src="/resource/njs/si/core_agile_pack.js" type="text/javascript"></script>
<script>
	Constants = {
	    ctx: '',
	    loginNo: '123',
	    loginName: '123',
	    groupId: '123'
	};
	
</script>


		
		<title>营业员登录人证比对接口</title>
		<link rel="stylesheet" href="/nresources/default/css/styleui.css" />
		<script language="javascript">
		
var tmp_accept = '20210327153631';
var file_local = 'C:\\WINDOWS\\temp\\';
var dz_flag = '1';
var headPath; //动作活体与静默活体图片路径
var num ;

    //手机拍照用包
    var timer = null;
	//检查客户端临时目录 jx20120731tianyang00
	try{
		var fso = new ActiveXObject("Scripting.FileSystemObject");
		if(!fso.FolderExists(file_local)){
			fso.CreateFolder(file_local);//创建临时文件目录
			var fdr=fso.GetFolder(file_local);
			fdr.attributes=2;//隐藏临时文件目录
		}
	}catch(e){
		alert("请检查浏览器安全设置!");
	}
	
	window.onload=function(){	
		//提示区域初始化
		 document.getElementById('PROMPTMSG').innerHTML = "设备状态显示区";
		document.getElementById('show_bSub').style.display='block';
		window.clipboardData.setData("Text","");
		document.getElementById('phonePhoto').style.display='block'; 
	}
	 
</script>
<script language="javascript">

    var tipId;
    //父页面
    var parent_win = window.dialogArguments;
     //var parent_win = window.opener;
	var isScan = false;


	//二代证读验设备获取身份认证信息
	var authxml="";
	var v_name="";
	var v_e_name="";
	var v_sex="";
	var v_nation="";
	var v_ethnic="";
	var v_birthday="";
	var v_address="";
	var v_card_no="360104198109240016";
	var v_issue_org="";
	var v_issue_date="";
	var v_b_valid_date="";
	var v_e_valid_date="";
	var v_remarks="";
	var v_remarks="";
	var v_projectFlag='JX';
	var file_src="";
	var picName="";
	var face_result=""
	var url="";  //在线平台url
	var params="";  //在线平台参数

//预览图像信息
function PreviewImg(picpath,area_h){
	try{
		file_src = picpath;
	    var newPreview = document.getElementById("newPreview");
	     
	 	while(newPreview.hasChildNodes()) //当div下还存在子节点时 循环继续
	    {
	        newPreview.removeChild(newPreview.firstChild);
	    }
	    var imgDiv = document.createElement("div");
	    document.body.appendChild(imgDiv);
	    imgDiv.style.width = "360px";   imgDiv.style.height = area_h;
	    imgDiv.style.filter=
	       "progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod = scale)"; 
	    imgDiv.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = picpath;
	    newPreview.appendChild(imgDiv);
	}catch(e){
		alert("重新加载！");
	}
}
	
	
//预览图像信息
function PreviewImg2(picpath,area_h){
	try{
		file_src = picpath;
	    var newPreview2 = document.getElementById("newPreview2");
	     
	 	while(newPreview2.hasChildNodes()) //当div下还存在子节点时 循环继续
	    {
	        newPreview2.removeChild(newPreview2.firstChild);
	    }
	 	 
 		var imgDiv = document.createElement("div");
	    document.body.appendChild(imgDiv);
	    imgDiv.style.width = "260px";   imgDiv.style.height = area_h;
	    //imgDiv.style.width = "360px";   imgDiv.style.height = "202px";
	    imgDiv.style.filter=
	       "progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod = scale)"; 
	    imgDiv.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = picpath;
	    newPreview2.appendChild(imgDiv);
	 	
	    
	}catch(e){
		alert("重新加载！");
	}
}	
	
//二代读卡证件读卡
function readByCardReader(){	
		
	/*document.getElementById('PROMPTMSG').innerHTML = "读取证件信息开始...";
	alert("C:\\WINDOWS\\temp\\"+"cert_"+"panda"+".jpg");
	PreviewImg("C:\\WINDOWS\\temp\\"+"cert_"+"panda"+".jpg","300px");
	document.getElementById('isreader').value="1";
	saveData();//报文字符串保存至粘贴板	
	alert(v_card_no);
	document.getElementById('PROMPTMSG').innerHTML = "读取证件信息结束...";*/
}
function readCard(){
	var ret_open=CardReader_CMCC.MutiIdCardOpenDevice(1000);
	if(ret_open!=0){
		ret_open=CardReader_CMCC.MutiIdCardOpenDevice(1001);
	}	

	if(ret_open==0){
		var cardType=document.getElementById("card_type").value ;	
		if(cardType==11){
			//多功能设备RFID读取
			var ret_getImageMsg=CardReader_CMCC.MutiIdCardGetImageMsg(cardType,file_local+"cert_head.jpg");
			if(ret_getImageMsg==0){
				//二代证正反面合成
				var xm =CardReader_CMCC.MutiIdCardName;					
				var xb =CardReader_CMCC.MutiIdCardSex;
				var mz =CardReader_CMCC.MutiIdCardPeople;
				var cs =CardReader_CMCC.MutiIdCardBirthday;
				var yx =CardReader_CMCC.MutiIdCardSigndate+"-"+CardReader_CMCC.MutiIdCardValidterm;
				var zz =CardReader_CMCC.MutiIdCardAddress;
				var qfjg =CardReader_CMCC.MutiIdCardOrgans;
				var zjhm =CardReader_CMCC.MutiIdCardNumber;
				var base64 =CardReader_CMCC.MutiIdCardPhoto;
				var mblj=file_local+"cert_model.bmp";
				var sclj=file_local + "cert_" + zjhm + ".jpg";
				var mbheads = file_local+"heads_model.bmp";
				var mbtails = file_local+"tails_model.bmp";
				var heads = file_local+"heads_" + tmp_accept + ".jpg";
				var tails = file_local+"tails_" + tmp_accept + ".jpg";
				var ret_cardEmerg=CardReader_CMCC.CardEmerg(xm,xb,mz,cs,yx,zz,qfjg,zjhm,base64,mblj,mbheads,mbtails,sclj,heads,tails);
				//保存信息
				if(ret_cardEmerg!=0){
					v_name=CardReader_CMCC.MutiIdCardName;
					v_e_name="";
					v_sex=CardReader_CMCC.MutiIdCardSex;
					v_nation="";
					v_ethnic=CardReader_CMCC.MutiIdCardPeople;
					v_birthday=CardReader_CMCC.MutiIdCardBirthday;
					v_address=CardReader_CMCC.MutiIdCardAddress;
					v_card_no=CardReader_CMCC.MutiIdCardNumber;
					v_issue_org=CardReader_CMCC.MutiIdCardOrgans;
					v_issue_date="";
					v_b_valid_date=CardReader_CMCC.MutiIdCardSigndate;
					v_e_valid_date=dealLongTerm(CardReader_CMCC.MutiIdCardValidterm);
					v_remarks="";
					PreviewImg(file_local + "cert_" + zjhm + ".jpg","350px");	
					
					if(v_e_valid_date == ""){
						rdShowMessageDialog("未读取到证件信息，请重试！",0);
						return false;
					}else{
						if(checkDateValid(v_e_valid_date)){
					    	document.getElementById('isreader').value="1";
						}else{
							//设置粘贴板数据为空
							window.clipboardData.setData("text","");
							rdShowMessageDialog("该证件已过有效期！",0);
							return false;
						}
					}
					if(base64 != "" && CardReader_CMCC.HeadsBase64 != "" && CardReader_CMCC.TailsBase64 != ""){
					     document.getElementById('isreader').value="1";
					}else{
					    document.getElementById('isreader').value="1";
						document.getElementById('PROMPTMSG').innerHTML = "读取证件信息结束...";
					}
					core.insertMachineLog('3', 'Y', 'bp095');
				}else{
					core.insertMachineLog('3', 'N', 'bp095');
					document.getElementById('PROMPTMSG').innerHTML = "二代证合成失败...";
				}
			}else{
				document.getElementById('PROMPTMSG').innerHTML = "获取信息失败...";
				core.insertMachineLog('3', 'N', 'bp095');
				return false;
			}
		}else if(cardType==3){				
			var ret_photo=CardReader_CMCC.MutiIdCardPhotograph(file_local+"cert_" + tmp_accept + ".jpg",cardType);
			PreviewImg(file_local+"cert_" + tmp_accept + ".jpg","270px");
			document.getElementById('isreader').value="1";
			document.getElementById('PROMPTMSG').innerHTML = "读取证件信息结束...";
		}else{
		
			//多功能设备OCR读取
			var ret_getImageMsg=CardReader_CMCC.MutiIdCardGetImageMsg(cardType,file_local+"cert_" + tmp_accept + ".jpg");
			//保存信息
			if(ret_getImageMsg==0){
				v_name=CardReader_CMCC.MutiIdCardName;
				v_e_name="";
				v_sex=CardReader_CMCC.MutiIdCardSex;
				v_nation="";
				v_ethnic=CardReader_CMCC.MutiIdCardPeople;
				v_birthday=CardReader_CMCC.MutiIdCardBirthday;
				v_address=CardReader_CMCC.MutiIdCardAddress;
				v_card_no=CardReader_CMCC.MutiIdCardNumber;
				v_issue_org=CardReader_CMCC.MutiIdCardOrgans;
				v_issue_date="";
				v_b_valid_date=CardReader_CMCC.MutiIdCardSigndate
				v_e_valid_date=dealLongTerm(CardReader_CMCC.MutiIdCardValidterm);
				v_remarks="";
				
				PreviewImg(file_local+"cert_" + tmp_accept + ".jpg","270px");
				
				if(v_e_valid_date == ""){
					rdShowMessageDialog("未读取到证件信息，请重试！",0);
					return false;
				}else{
					if(checkDateValid(v_e_valid_date)){
					    document.getElementById('isreader').value="1";
					}else{
						//设置粘贴板数据为空
						window.clipboardData.setData("text","");
						rdShowMessageDialog("该证件已过有效期！",0);
						return false;
					}
				}
				core.insertMachineLog('3', 'Y', 'bp095');
				document.getElementById('isreader').value="1";
				document.getElementById('PROMPTMSG').innerHTML = "读取证件信息结束...";
				return false;
			}else{
				core.insertMachineLog('3', 'N', 'bp095');
				document.getElementById('PROMPTMSG').innerHTML = "获取信息失败...";
				return false;
			}
		}
	}else{
		core.insertMachineLog('3', 'N', 'bp095');
		document.getElementById('PROMPTMSG').innerHTML = "打开设备失败...";
	
	}
	//关闭设备
	var ret_close=CardReader_CMCC.MutiIdCardCloseDevice();
	document.getElementById('bReadByMulti').disabled = '';
}
function readByMulti(){
	document.getElementById('bReadByMulti').disabled = 'disabled';
	document.getElementById('PROMPTMSG').innerHTML = "读取证件信息开始...";
	window.setTimeout(readCard, 100); 
}

function exeInsertBack(responseValue) {
	responseValue=responseValue.replace(/(^\s*)|(\s*$)/g,"");
	if(responseValue == "0"){
		document.getElementById('PROMPTMSG').innerHTML = "证件采集成功,读取证件信息结束...";
	}else{
		document.getElementById('PROMPTMSG').innerHTML = "证件采集失败,读取证件信息结束...";
	}
}


function saveData(){
	//补录时可以添加附件
	isScan=true;
	
	//设置粘贴板数据为空
	window.clipboardData.setData("text","");
	
	authxml="{\"result\":\""+face_result+"\",\"v_card_no\":\""+v_card_no+"\"}";
	//设置粘贴板数据
	window.clipboardData.setData("text",authxml);
	
		
}

//判断设备是否注册
function equCheckRegister(){
	var product_id = "111111111";
	//获取营业台席PC机 IP地址 MAC地址 
	var locator =new ActiveXObject("WbemScripting.SWbemLocator");
	var service = locator.ConnectServer(".");
	var properties = service.ExecQuery("SELECT * FROM Win32_NetworkAdapterConfiguration");
	var e =new Enumerator(properties);
	for (; !e.atEnd(); e.moveNext()) {
		var p = e.item();
		if (p.IPAddress==null) {
			continue;
		}
		var client_ip = p.IPAddress(0);
		var client_mac = p.MACAddress.replace(/\:/g,'-');
	}
	//zhaoxin@20121011@判断设备是否注册
	var state = (checkequ(product_id,client_ip,client_mac));
	if(state == true){
		rdShowMessageDialog("设备已注册",2);
	}else{
		rdShowMessageDialog("设备未注册",1);
	}		
}


function confAuth(){
	if(authxml=="") alert("未获取到认证信息！");
	window.close();
}

function trim(str){ //删除左右两端的空格
	return str.replace(/(^\s*)|(\s*$)/g, "");
}
function replaceContent(str){
	return str.replace(/(\-)|(\.)/g,"");
}


//store cookie value with optional details as needed @sc20120510tianyang00
function setCookie(name, value, expires, path, domain, secure)
{
	document.cookie = name + "=" + escape(value) +
        ((expires) ? "; expires=" + expires : "") +
        ((path) ? "; path=" + path : "") +
        ((domain) ? "; domain=" + domain : "") +
        ((secure) ? "; secure" : "");
}
//utility function to retrieve an expiration data in proper format @sc20120510tianyang00
function getExpDate(days, hours, minutes)
{
	var expDate = new Date();
    if(typeof(days) == "number" && typeof(hours) == "number" && typeof(hours) == "number")
    {
        expDate.setDate(expDate.getDate() + parseInt(days));
        expDate.setHours(expDate.getHours() + parseInt(hours));
        expDate.setMinutes(expDate.getMinutes() + parseInt(minutes));
        return expDate.toGMTString();
    }
}
//将长期有效转成20300101
function dealLongTerm(dateStr){
	if(dateStr.indexOf("长期") !=-1){
		return "20300101";
	}else{
		return dateStr;
	}
}
//个位月、日前面补0
function formateStr(numb){
	if(numb<10){
		return "0"+numb;
	}else{
		return ""+numb;
	}
}
//校验身份证件的有限期
function checkDateValid(dateStr){
    var sysdateStr = '20210327';
	return new Number(sysdateStr) < new Number(dateStr);
}



//静默活体检测
function face_jmtesting(){
	return;

    	//设置文件名头部,默认为(cert_)
    	var		strFileHeader ="cert_";
    	AgCardReaderAndCapture.AgSetLiveImgHeader(strFileHeader);
    	
    	var 	strPath="C:/WINDOWS/Temp/";
    //	var		strPhotoId = "silent";
    	num = Math.ceil(Math.random()*100);  
    	var		strPhotoId = tmp_accept+num;
    	var     waterbase64='';
    	var 	nRet = AgCardReaderAndCapture.AgGetLiveFaceImg(strPath,strPhotoId);
    	var		nErrMsg = "";
    	if(nRet != 0)
    	{
    		nErrMsg = AgCardReaderAndCapture.AgGetLastError(nRet);
    		rdShowMessageDialog("检测失败:"+nErrMsg+",请重新检测!",1);
    	}
    	else
    	{   
    		  PreviewImg2(strPath+strFileHeader+strPhotoId+"_0.jpg","300px");
    		 // ret = AgObj1.AgDisplayPic(strPath+strFileHeader+strPhotoId+"_0.jpg");
    		  headPath=strPath+strFileHeader+strPhotoId+"_0.jpg";
    		  //HWPostil1.DeleteLocalFile(strPath+strFileHeader+strPhotoId+"_2.jpg");----
    		  //HWPostil1.DeleteLocalFile(strPath+strFileHeader+strPhotoId+"_1.jpg");----
    		  document.getElementById('isphoto').value="9";
    			
    		
    	}
 }


//人证比较接口
function compareInte(){
	 
	document.getElementById('bReadByMulti').disabled='disabled';
	document.getElementById('bReadByCardReader').disabled='disabled';
	document.getElementById('bcompareInte').disabled='disabled';
	document.getElementById('bcompareInte1').disabled='disabled';
	var isphoto = document.getElementById('isphoto').value;
 	HWPostil1.HttpInit();
 	HWPostil1.HttpAddPostString("tmp_accept",tmp_accept);
   	HWPostil1.HttpAddPostFile("files","C:\\Windows\\Temp\\face.jpg");
	HWPostil1.HttpAddPostFile("files","‪C:\\Windows\\Temp\\cert_panda.jpg");
	
	var message = HWPostil1.HttpPost("http://10.180.214.106:18080/bp095Ajax/uploadFileLogin");				
	
	document.getElementById('bReadByMulti').disabled='';
	document.getElementById('bReadByCardReader').disabled='';
	document.getElementById('bcompareInte').disabled='';
	document.getElementById('bcompareInte1').disabled='';
	face_result="0";
	var strs= message.split(",");
    //var resflag = strs[0];
	var resflag = "1";
	if(resflag=="1"){
	    face_result="1";
	    saveData();
        //rdShowMessageDialog("！比对结果为："+strs[1]+"分,最低分值为："+strs[2]+"分",2);
        //HWPostil1.DeleteLocalFile(file_local+"picture.JPG");-----
        //HWPostil1.DeleteLocalFile(file_local+"cert_head.jpg");----
        //HWPostil1.DeleteLocalFile(file_local+"heads_" + tmp_accept + ".jpg");----
        //HWPostil1.DeleteLocalFile(file_local+"tails_" + tmp_accept + ".jpg");----
        //HWPostil1.DeleteLocalFile(file_local+"cert_" + v_card_no + ".jpg");----
	    //HWPostil1.DeleteLocalFile(headPath);
        window.close();
    }else if(resflag=="2"){
   	 	saveData();
        rdShowMessageDialog("人证比对不通过！比对结果为："+strs[1]+"分,最低分值为："+strs[2]+"分",1);
        return false;
    }else if(resflag=="3"){
   	 	saveData();
       	rdShowMessageDialog("未找到人像信息，请重新拍摄!",1);
       	return false;
    }else if(resflag=="4"){
   	 	saveData();
        rdShowMessageDialog("程序异常，请重新发起人证比对流程!",1);
        return false;
    }else{
    	saveData();
        rdShowMessageDialog("人证比对不通过！",1);
    }

	    ret = AgObj1.AgDisplayPic("");
	    //HWPostil1.DeleteLocalFile(headPath);----
   
}

function GetRandomNum(Min,Max)
{   
var Range = Max - Min;   
var Rand = Math.random();   
return(Min + Math.round(Rand * Range));   
}   
 
	
/* //得到拍照照片		
function getPic(){
	var num = GetRandomNum(100,999);   
	var isphoto=document.getElementById('isphoto').value;
	if(isphoto=="1"||isphoto=="2"){
		jQuery.ajax({
		    url: "/bp095.go?method=getPic",
		    type: "POST",
		    async: false,
		    data: {"tmpAccept":tmp_accept,"RandomNum":num},
		    dataType: "json",
        	success: function(msg){
        		if(msg.retCode=="0"){
        			$("#phonePhoto").html('<DIV align="center" id="photoD"><img src="'+msg.retValue+'?randomNum='+num+' width="350" height="350"/></DIV>');
        		    var msgval=msg.retValue;
        		    picName=msgval.substring(msgval.lastIndexOf("/")+1,msgval.length);
        		    document.getElementById('isphoto').value="2";
        		}
       		}
    	});
    }
} */

//摄像头拍照
function camera(){
	var isphoto = document.getElementById('isphoto').value;
	if(isphoto == '2'){
       	rdShowMessageDialog("手机拍照后不可以使用摄像头拍照!",1);
        return false;
	}
	var ret = AgObjCard.AgCameraSaveFile(file_local + tmp_accept + "_card.jpg");
	if(ret != 0) {
		alert('拍照失败或没有提交拍照'+ret);
	} else {
		ret = AgObjCard.AgDisplayPic(file_local + tmp_accept + "_card.jpg");
		if(ret<0){
			alert("加载预览图片失败ret="+ret);
		}else{
			alert("加载预览图片成功");
			//isCamera = 1 ;
		}
		if(ret == 0){
			document.getElementById('isreader').value = '1';
		}
	}
}

//真人检测
function face_testing(){
	
	if(dz_flag == 1){
		rdShowMessageDialog("  '人脸识别'  已停用 ；请您使用   '静默人脸识别'  进行人像采集。如果无法使用，请到4A系统首页下载新无纸化控件并按教程文档安装。感谢支持！",0);
		return false;
	}
	
	//AgSetConfigInfo根据需要进行设置，可选，不设置默认读取配置文件中的值；设置后优先选取设置的值
	//AgObj1.AgSetConfigInfo("LiveDetect","1");
	AgObj2.AgSetConfigInfo("LiveDetectLevel","1");//设置活体检测难度（1最低、2中等、3最高（非高清摄像头设置为1））
	AgObj2.AgSetConfigInfo("LiveDetectNum","2");  //设置活体检测次数
	AgObj2.AgSetConfigInfo("CameraDirection","0"); //设置摄像头方向（0正常、1顺时针90度、2逆时针90度）
	AgObj2.AgSetConfigInfo("License","MTcyNTE2bm9kZXZpY2Vjd2F1dGhvcml6ZZ3m5Ofl5+Xq3+bg5efm5Of+5efl4Obg5Yjm5uvl5ubrkeXm5uvl5uai6+Xm5uvl5uTm6+Xm5uDm6uvn6+fr5+DV5+vn6+fr59Xn5ebl5eY="); //设置授权码（此为测试授权码）
  	AgObj2.AgSetConfigInfo("Width","480");  //设置摄像头显示图像宽度
  	AgObj2.AgSetConfigInfo("Height","320"); //设置摄像头显示图像高度
	var ret = AgObj2.AgLiveDetection();
	var paramJson = eval("(" + ret + ")");//转化JSON
	
	var ret = AgObj1.AgBase64ToFile(paramJson['Image'],file_local + tmp_accept + ".jpg");
	headPath=file_local + tmp_accept + ".jpg";
	if(ret != 0) {
		alert('活体检测图片转换失败'+ret);
	} else {
		//ret = AgObj1.AgDisplayPic(file_local + tmp_accept + ".jpg");
		PreviewImg2(headPath,"300px");
		document.getElementById('isphoto').value = '3';
		
	}
}



//港澳台读卡
function ReadGATCard()
{		
		 //读卡操作
		var nRet = -1;
		var strErrMsg="";
		nRet = AgObj3.AgIDReadCard();
		if(0 != nRet)
		{//失败的情况
		 strErrMsg = AgObj3.AgGetLastError(nRet);
		 rdShowMessageDialog("读卡失败,错误描述!"+ strErrMsg,1);
		}
		v_name = AgObj3.AgGetCardInfo(0);
		//alert("姓名: " +v_name);
		v_e_name ;
		//性别
		v_sex = AgObj3.AgGetCardInfo(1);
		//alert("性别: " + AgObj3.AgGetCardInfo(1));
		//民族
		v_ethnic = AgObj3.AgGetCardInfo(2);
		//alert("民族: " + AgObj3.AgGetCardInfo(2));
		//出生
		v_birthday = AgObj3.AgGetCardInfo(3);
		//alert("出生: " + AgObj3.AgGetCardInfo(3));
		//住址
		v_address = AgObj3.AgGetCardInfo(4);
		//alert("住址: " + AgObj3.AgGetCardInfo(4));
		//身份号码
		v_card_no = AgObj3.AgGetCardInfo(5);
		//alert("身份号码: " + AgObj3.AgGetCardInfo(5));
		//签发机关
		v_issue_org = AgObj3.AgGetCardInfo(6);
		//alert("签发机关: " + AgObj3.AgGetCardInfo(6));
		//开始有效期
		v_b_valid_date = AgObj3.AgGetCardInfo(7);
		//alert("开始有效期: " + AgObj3.AgGetCardInfo(7));
		//结束有效期
		v_e_valid_date = AgObj3.AgGetCardInfo(8);
		//alert("结束有效期: " + AgObj3.AgGetCardInfo(8));
		//头像Base64
		var base64Str = AgObj3.AgGetCardInfo(11);
		//alert("头像Base64: " + AgObj3.AgGetCardInfo(11));
		pass_no =  AgObj3.AgGetCardInfo(201);
		//alert("通行证号码: " + AgObj3.AgGetCardInfo(201));
		//签发次数
		issue_num =  AgObj3.AgGetCardInfo(202);
		//alert("签发次数: " + AgObj3.AgGetCardInfo(202));
		 var area_type="";
		//证件类型
		nType = AgObj3.AgGetCardType();
			//alert("nType ======="+nType );
			//香港澳门居民居住证
		 if(102 == nType || 103 == nType){
			alert("香港澳门居民居住证");
			area_type="GA";
		}
		else if(104 == nType)
		{//台湾居民居住证
			alert("台湾居民居住证");
			area_type="TW";
		}
		else
		{//未知类型
			alert("其他类型证件:" + nType);
		} 
		//二代证正反面合成
		    var xm =v_name;	
			var xb =v_sex;
			var mz =v_ethnic;
			var cs =v_birthday;
			var yx =v_b_valid_date+"-"+v_e_valid_date;
			var zz =v_address;
			var qfjg =v_issue_org;
			var zjhm =v_card_no;
			var base64 =base64Str;
			var txzhm =pass_no;
			var qfcs = issue_num; 
			var mbtails = file_local+ "cert_" + zjhm + ".jpg";
				var heads = file_local+"heads_" + tmp_accept + ".jpg";
				var tails = file_local+"tails_" + tmp_accept + ".jpg";
			
			 /*  base64 ="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";
			  
			   var ret_c = AgObj3.AgCardEmergHKMT("张三", "男",  "19840113", "20181012"+ "-" + "20281012",
					"哈尔滨浦发大厦", "哈尔滨", "41138119840113421X","212991281","2", base64 ,
					"", "", "", mbtails, heads, tails);   */
		  var ret_c = AgObj3.AgCardEmergHKMT(xm, xb, cs, yx,zz, qfjg, zjhm,txzhm,qfcs, base64 ,
					"", "", "", mbtails,heads, heads);  
			//保存信息
			if(ret_c==0){
				PreviewImg(mbtails,"350px");
				
				if(v_e_valid_date == ""){
					rdShowMessageDialog("未读取到证件信息，请重试！",0);
					return false;
				}else{
					if(checkDateValid(v_e_valid_date)){
					//saveGATData();//报文字符串保存至粘贴板
					document.getElementById('isreader').value="1";
					}else{
						//设置粘贴板数据为空
						window.clipboardData.setData("text","");
						rdShowMessageDialog("该证件已过有效期！",0);
						return false;
					}
				}
				core.insertMachineLog('3', 'Y', 'bp095');
			}else{
			    core.insertMachineLog('3', 'N', 'bp095');
				document.getElementById('PROMPTMSG').innerHTML = "港澳台证件合成失败...";
			}
	

}
	
function closewin(){ 
  HWPostil1.DeleteLocalFile(file_local+"cert_head.jpg");
  HWPostil1.DeleteLocalFile(file_local+"heads_" + tmp_accept + ".jpg");
  HWPostil1.DeleteLocalFile(file_local+"tails_" + tmp_accept + ".jpg");
  HWPostil1.DeleteLocalFile(file_local + tmp_accept + ".jpg");
} 
window.onunload=closewin;

		
</script> 
	</head>
	
	<style>
		
		
	</style>
	<body>
		
			
			 <div id="PROMPTMSG" style="color: blue; font-size: 12px;"   align="CENTER"></div>
		<div class="card-left">
			
			<div class="card" >
				
				
			    <div class="card-body">
			    	
			    	<div class="card-header">
					
						<div class="img-left">
							
						</div>
						
						<span class="card-header-text">
							
							多功能识别
						</span>
				    </div>
			    	
			    	<div  class="card-line">
			    		
			    		<div class="card-btn" onClick="readByMulti()" id="bReadByMulti">
			    		<div class="card-btn-img img-read-card"></div>
			    		<div class="card-btn-desc" >
			    			读卡 
			    			<br/><br/>
			    		</div>
			    	</div>
			    	<div class="card-btn" onClick="face_jmtesting()" id="face_testing_2">
			    		<div class="card-btn-img img-face-static"></div>
			    		<div class="card-btn-desc" >
			    			人脸识别(静默)
			    		</div>
			    	</div>
			    	<div class="card-btn"  onClick="compareInte()" id="bcompareInte">
			    		<div class="card-btn-img img-card-witness"></div>
			    		<div class="card-btn-desc" >
			    			人证比对
			    			<br/><br/>
			    		</div>
			    	</div>
			    		
			    	</div>
			    	
			    	 <div class="card-load" id="newPreview">
			    		
			    		<div  class="card-load-div">
			    			
			    			<div class="card-load-img"></div>
			    			<div class="card-load-desc">
			    				
			    				图片预览
			    			</div>
			    		</div>
			    	
			    	</div>
			    	
			    </div>
			   
				
			</div>
		</div>
		
		<div class="card-right" >
			
			<div class="card" >
				
			    
			    <div class="card-body">
			    	
			    	<div class="card-header">
					
						<div class="img-left">
							
						</div>
						
						<div class="card-header-text">
							
							二代证读验
						</div>
				    </div>
			    	
			    	<div  class="card-line">
			    	
			    	<div class="card-btn" onClick="readByCardReader()" id="bReadByCardReader">
			    		<div class="card-btn-img img-read-card"></div>
			    		<div class="card-btn-desc" >
			    		  读卡
			    		<br/><br/>
			    		</div>
			    	</div>
			    	<div class="card-btn" onClick="face_jmtesting()" id="face_testing_2">
			    		<div class="card-btn-img img-face-static"></div>
			    		<div class="card-btn-desc" >
			    			人脸识别(静默)
			    		</div>
			    	</div>
			    	<div class="card-btn"  onClick="compareInte()" id="bcompareInte1">
			    		<div class="card-btn-img img-card-witness"></div>
			    		<div class="card-btn-desc" >
			    			人证比对
			    			<br/><br/>
			    		</div>
			    	</div>
			    	</div>
			    	
			    	 <div class="card-load" id="newPreview2">
			    		
			    		<div class="card-load-div">
			    			
			    			<div class="card-load-img"></div>
			    			<div  class="card-load-desc">
			    				
			    				图片预览
									
			    			</div>
			    		</div>
			    	
			    	</div>
			    	
			    </div>
				
			</div>
			<div id='show_bSub'>
							<input type="hidden" value="0" id="isreader">
							<input type="hidden" value="0" id="isphoto">
							<input type="hidden" value="11" id="card_type">
							
			</div>
			<div id='phonePhoto' style="height: 360px" style="display: none;">
								</div>
		</div>

			
			
	</body>
</html>
<!-- sc20120419dingyi00 身份识别设备DLL检查-->
<script language=javascript src="/resource/ocx/LoadCardReaderAgile.js"></script>
<script language=javascript src="/resource/ocx/LoadGatCardReader.js"></script>
<OBJECT id="AgObj1" style="height:0px; width:0px; LEFT: 0px; TOP: 0px" classid="clsid:9082D267-2D37-4D53-B580-1E82D3696A2B" codebase="/resource/ocx/AgCamera.cab#version=2,0,4,1010"></OBJECT>
<OBJECT id="AgObj2" name="AgObj2" classid="clsid:55CD9D6D-CD7B-448D-B508-5BC290C7B51C" codebase="AgFaceContrast.ocx" style="HEIGHT: 0px;WIDTH:0px"></OBJECT> 
<object id="AgCardReaderAndCapture" name="AgCardReaderAndCapture" classid="clsid:96DF2342-9FE0-4D7A-8097-78A3A188707C" codebase="AgCardReader.ocx" style="HEIGHT: 0px;WIDTH:0px"></object>
<div id="show_HWPostil1" align="center" style="display: none;">
	<script language=javascript src="/resource/ocx/LoadAip.js"></script>
</div>
<script language=javascript>
   
	//判断设备类型
	var fso = new ActiveXObject("Scripting.FileSystemObject");
	if(!fso.FileExists("C:/WINDOWS/system32/CMCC_IDCard.dll")){  
		document.getElementById('trCardReader').style.display='none';
	}
	if(!fso.FileExists("C:/WINDOWS/system32/MutiIdCard.dll")){  
		document.getElementById('trMulti').style.display='none';
	}
</script> 
