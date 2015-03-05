package web.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.log4j.Logger;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;
import web.model.UserForm;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

@Controller
@RequestMapping("/")
public class MainController {
	private static final Logger log = Logger.getLogger(MainController.class); 

	private ObjectMapper jsonMapper = new ObjectMapper();

	@RequestMapping(value="/post_form", method=RequestMethod.POST)
	public @ResponseBody UserForm post_form(@ModelAttribute("user") UserForm user) {
/*	public String test(@RequestBody UserForm user) {
	public String test(@RequestBody MultiValueMap<String, String> map) {
	public String test(HttpServletRequest request) {
	public String test(@RequestParam(value="email", required=false) String email) {*/
//		return "redirect:/login.html";
		user.setLogin_id("Lee");
		return user;
	}

    @RequestMapping(value="/post_json", method=RequestMethod.POST)
    public @ResponseBody UserForm post_json(@RequestBody UserForm user) {
        user.setLogin_id("Lee");
        return user;
    }
	
	@RequestMapping(value="/test")
	public ModelAndView testCallback(HttpServletRequest request, HttpServletResponse response) throws Exception {
		String result = "{status:true}";
		Map<String, Object> model = new HashMap<String, Object>();
		model.put("email", "andy@wavegis.com.tw");
//		response.getWriter().write(result);
//		response.sendRedirect("../register4openid.html?"+result);
		return new ModelAndView("register4openid", model);
	}
	
}
