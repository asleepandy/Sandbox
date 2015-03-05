package web.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;
import web.model.UserForm;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
@ContextConfiguration(locations = {
		"classpath*:spring-conf.xml"})
public class MainControllerTest {
	
	@Autowired
	private WebApplicationContext wac;
	
	private MockMvc mockMvc;
    private ObjectMapper m = new ObjectMapper();
	
	@Before
	public void setup() {
		this.mockMvc = MockMvcBuilders.webAppContextSetup(this.wac).build();
	}

    @Test
    public void getTest() throws Exception {

    }

	@Test
	public void postTest() throws Exception {
		UserForm user = new UserForm();
		user.setLogin_pwd("admin");

		ResultActions r =  this.mockMvc.perform(
                post("/post_form").param("login_pwd", "123").accept("application/json;charset=UTF-8"));
		r.andExpect(status().isOk())
		.andExpect(content().contentType("application/json;charset=UTF-8"))
		.andExpect(jsonPath("$.login_pwd").value("123"));

        ResultActions r1 =  this.mockMvc.perform(
                post("/post_json").contentType(MediaType.APPLICATION_JSON)
                        .content(m.writeValueAsString(user)).accept("application/json;charset=UTF-8"));
        r1.andExpect(status().isOk())
                .andExpect(content().contentType("application/json;charset=UTF-8"))
                .andExpect(jsonPath("$.login_pwd").value("admin"));
//		MvcResult mr = r.andReturn();
	}
}
