package web.model;

import org.apache.commons.beanutils.DynaBean;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;


public class UserForm extends SystemBean {
	private int		user_id;	//帳號流水號
	private	int		unit_id;	//所屬單位代碼
	private	String	user_no;	//員工編號
	private	String	user_name;	//使用者名稱
	private	String	login_id;	//使用者帳號
	private	String	login_pwd;	//使用者密碼
	private	String	identity;	//身分證字號
	private	String	phone;		//連絡電話
	private	String	cellphone;	//手機
	private	String	fax;		//傳真
	private String 	address;	//住址
	private	String	email;		//E-mail
	private	String	title_name;	//職稱編號 (sd.code_type(05) 再與code_type_id關連 )
	private String 	employ_start;	//在職起始時間
	private String  employ_end;	//在職結束時間
	private String  enable_time;	//帳號啟用時間
	private String  expire_time;	//帳號到期時間
	private	String	note;		//備註

	private	String	group_id = "-1";	//群組代碼 (sd.group.group_id )

	private String  login_ip;
	
	private String  companyName="";
	private	String	unit_no;	//所屬單位編號 (與sd._uint.unit_no 關連)
	private	String	unit_name;	//所屬單位名稱  (sd._user.unit_no 與 sd._uint.unit_no 關連 取得 sd._unit.unit_name )
	private	String	alarm_group_no;	//資料權限群組編號
	
	@Override
	public String getKey() {
		return String.valueOf(getUser_id());
	}

	public String getCompanyName() {
		return companyName;
	}

	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}

	public String getIdentity() {
		return identity;
	}

	public void setIdentity(String identity) {
		this.identity = identity;
	}

	public int getUser_id() {
		return user_id;
	}

	public void setUser_id(int user_id) {
		this.user_id = user_id;
	}

	public int getUnit_id() {
		return unit_id;
	}

	public void setUnit_id(int unit_id) {
		this.unit_id = unit_id;
	}

	public String getKey_id(){
		return String.valueOf(user_id);
	}

	public String getLogin_ip() {
//		if(null == userIP) userIP = Sessions.getCurrent().getRemoteAddr(); 
		return login_ip;
	}
	
	public void setLogin_ip(String login_ip) {
		this.login_ip = login_ip;
	}

	/**
	 * @return 使用者帳號
	 */
	public String getLogin_id() {
		return login_id;
	}
	
	/**
	 * 設定 使用者帳號
	 * @param login_id
	 */
	public void setLogin_id(String login_id) {
		this.login_id = login_id;
	}
	
	/**
	 * 
	 * @return 使用者名稱
	 */
	public String getUser_name() {
		return user_name;
	}
	
	/**
	 * 設定 使用者名稱
	 * @param user_name
	 */
	public void setUser_name(String user_name) {
		this.user_name = user_name;
	}
	
	/**
	 * 
	 * @return 所屬單位編號 (與sd._uint.unit_no 關連)
	 */
	public String getUnit_no() {
		if(unit_no == null){
			unit_no = "";
		}
		return unit_no;
	}
	
	/**
	 * 設定 所屬單位編號(與sd._uint.unit_no 關連)
	 * @param unit_no
	 */
	public void setUnit_no(String unit_no) {
		this.unit_no = unit_no ==null ? null :unit_no;
	}
	
	/**
	 * 
	 * @return 單位名稱
	 */
	public String getUnit_name() {
		return unit_name;
	}
	
	/**
	 * 設定 單位名稱
	 * @param unit_name
	 */
	public void setUnit_name(String unit_name) {
		this.unit_name = unit_name;
	}
	
	/**
	 * @return 職稱代碼
	 */
	public String getTitle_name() {
		if(title_name == null){
			title_name = "";
		}
		return title_name;
	}
	
	
	/**
	 * @return 資料權限群組編號
	 */
	public String getAlarm_group_no() {
		return alarm_group_no;
	}

	/**
	 * @param alarm_group_no 資料權限群組編號
	 */
	public void setAlarm_group_no(String alarm_group_no) {
		this.alarm_group_no = alarm_group_no;
	}

	/**
	 * 設定 職稱代碼
	 * @param title_name
	 */
	public void setTitle_name(String title_name) {
		if(title_name == null){
			title_name = "";
		}
		this.title_name = title_name;
		
	}
	
	/**
	 * 
	 * @return 群組代碼
	 */
	public String getGroup_id() {
		return group_id;
	}
	
	/**
	 * 設定 群組代碼
	 * @param group_id
	 */
	public void setGroup_id(String group_id) {
		this.group_id = group_id !=null ? group_id : null;
	}

	/**
	 * 
	 * @return 電話號碼
	 */
	public String getPhone() {
		return phone;
	}
	
	/**
	 * 設定 電話號碼
	 * @param phone
	 */
	public void setPhone(String phone) {
		this.phone = phone;
	}

	/**
	 * 
	 * @return 行動電話號碼
	 */
	public String getCellphone() {
		return cellphone;
	}
	
	/**
	 * 設定 行動電話號碼
	 * @param cellphone
	 */
	public void setCellphone(String cellphone) {
		this.cellphone = cellphone;
	}
	
	/**
	 * 
	 * @return 傳真號碼
	 */
	public String getFax() {
		return fax;
	}
	
	/**
	 * 設定 傳真號碼
	 * @param fax
	 */
	public void setFax(String fax) {
		this.fax = fax;
	}
	
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	/**
	 * 
	 * @return 電子郵件(E-mail)
	 */
	public String getEmail() {
		return email;
	}
	
	/**
	 * 設定 電子郵件(E-mail)
	 * @param email
	 */
	public void setEmail(String email) {
		this.email = email;
	}
	
	/**
	 * 
	 * @return 備註
	 */
	public String getNote() {
		return note;
	}
	
	/**
	 * 設定 備註
	 * @param note
	 */
	public void setNote(String note) {
		this.note = note;
	}

	/**
	 * @return 員工編號
	 */
	public String getUser_no() {
		return user_no;
	}
	
	/**
	 * 設定 員工編號
	 * @param user_no
	 */
	public void setUser_no(String user_no) {
		this.user_no = user_no;
	}

	/**
	 * @return 使用者密碼
	 */
	public String getLogin_pwd() {
		return login_pwd;
	}

	/**
	 * 設定 使用者密碼
	 * @param login_pwd
	 */
	public void setLogin_pwd(String login_pwd) {
		this.login_pwd = login_pwd;
	}

	public String getEmploy_start() {
		return employ_start;
	}

	public void setEmploy_start(String employ_start) {
		this.employ_start = employ_start;
	}

	public String getEmploy_end() {
		return employ_end;
	}

	public void setEmploy_end(String employ_end) {
		this.employ_end = employ_end;
	}

	public String getEnable_time() {
		return enable_time;
	}

	public void setEnable_time(String enable_time) {
		this.enable_time = enable_time;
	}

	public String getExpire_time() {
		return expire_time;
	}

	public void setExpire_time(String expire_time) {
		this.expire_time = expire_time;
	}
	
	public boolean isExpired() {
		boolean b = false;
		try {
			if(this.expire_time != null && !this.expire_time.isEmpty()) {
				SimpleDateFormat f = new SimpleDateFormat("yyyy-MM-dd");
				b = f.parse(this.expire_time).before(new Date());
			}
		} catch (ParseException e) {
			e.printStackTrace();
		}
		return b;
	}

	/**
	 * <p>共用方法 : 將DynaBean轉換為UserForm</p>
	 * <p>DynaBean欄位中須包含主鍵user_id</p>
	 * @param bean
	 * @return
	 */
	@Deprecated
	public static UserForm getUserForm(DynaBean bean) {
		if(bean.get("user_id") == null) return null;
		UserForm form = new UserForm();
		form.setUser_id((Integer)bean.get("user_id"));
		if(bean.get("user_name") != null)
			form.setUser_name(bean.get("user_name").toString());
		if(bean.get("group_id") != null)
			form.setGroup_id(bean.get("group_id").toString());
		return form;
	}
	
	public boolean isAdministrator() {
		return getGroup_id().equals("1");
	}
	
	@Deprecated
	public HashMap<String,Object> convertToMap(){
		HashMap<String,Object> map = new HashMap<String, Object>();
		map.put("login_id",login_id);
		map.put("login_pwd", login_pwd);
		map.put("user_name", user_name);
		map.put("identity",identity);
		map.put("unit_no", (unit_no!=null) && unit_no.equals("null")?null:unit_no);
		map.put("unit_name", unit_name);
		map.put("title_name", title_name);
		map.put("group_id",(group_id!=null) && group_id.equals("null")?null: group_id);
		map.put("phone", phone);
		map.put("cellphone", cellphone);
		map.put("fax", fax);
		map.put("email", email);
		map.put("note", note);
		map.put("user_no", user_no);
		map.put("create_user", getCreate_user());
		map.put("update_user", getUpdate_user());
		map.put("deleted",getDeleted());
		map.put("unit_id",unit_id);
		return map;
	}

}
