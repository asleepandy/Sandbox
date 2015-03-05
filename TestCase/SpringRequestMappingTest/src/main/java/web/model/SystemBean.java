package web.model;

import org.apache.commons.lang.builder.ToStringBuilder;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;

/**
 * 系統使用者操作系統所產生的資料, 需記錄其資料狀態、新增及修改相關的人與時間,
 * 所以建立此抽象層class 
 */
public abstract class SystemBean {
	public static final int STATUS_AVAILABLE = 0x00;
    public static final int STATUS_DISABLE   = 0x01;
    public static final int STATUS_DELETED   = 0x02;

	private int 		deleted;			//狀態
	private int 		create_user;		//建立者id
	private Timestamp   create_time;		//建立時間
	private int 		update_user;		//維護者id
	private Timestamp   update_time;		//維護時間
	private Timestamp	created_at_ = new Timestamp(System.currentTimeMillis());
	private Timestamp	updated_at_;
	
	protected SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssZ");
	
	public abstract String getKey();

	public String toString() {
        return ToStringBuilder.reflectionToString(this);
    }
	
	public void modifyBy(int user_id) {
		setCreate_user(user_id);
		setUpdate_user(user_id);
	}

	public boolean isEnable() {
		return getDeleted()==STATUS_AVAILABLE;
	}
	
	public void disable() {
		setDeleted(isDisable()?STATUS_AVAILABLE:STATUS_DISABLE);
	}
	
	public boolean isDisable(){
		return getDeleted()==STATUS_DISABLE;
	}
	
	public void delete() {
		setDeleted(STATUS_DELETED);
	}
	
	public boolean isRemoved() {
		return getDeleted()==STATUS_DELETED;
	}
	
	public String getStatus() {
		if(isRemoved()) return "刪除";
		if(isDisable()) return "停用";
		return "啟用";
	}
	
	public int getDeleted() {
		return deleted;
	}
	public void setDeleted(int deleted) {
		this.deleted = deleted;
	}
	public int getCreate_user() {
		return create_user;
	}
	public void setCreate_user(int create_user) {
		this.create_user = create_user;
	}
	public Timestamp getCreate_time() {
		return create_time;
	}
	public void setCreate_time(Timestamp create_time) {
		this.create_time = create_time;
	}
	public int getUpdate_user() {
		return update_user;
	}
	public void setUpdate_user(int update_user) {
		this.update_user = update_user;
	}
	public Timestamp getUpdate_time() {
		return update_time;
	}
	public void setUpdate_time(Timestamp update_time) {
		this.update_time = update_time;
	}

	public String getCreated_at() {
		if(created_at_ == null) return "";
		return sdf.format(created_at_);
	}

	public String getUpdated_at() {
		if(updated_at_ == null) return "";
		return sdf.format(updated_at_);
	}

	public void setCreated_at_(Timestamp created_at) {
		this.created_at_ = created_at;
	}

	public Timestamp getCreated_at_() {
		return created_at_;
	}

	public void setUpdated_at_(Timestamp updated_at) {
		this.updated_at_ = updated_at;
	}

	public Timestamp getUpdated_at_() {
		return updated_at_;
	}
	
	public static void main(String[] args) {
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssZ");
		Timestamp t = new Timestamp(System.currentTimeMillis());
		System.out.println(sdf.format(t));
	}
}
