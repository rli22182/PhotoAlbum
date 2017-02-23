package com.alikian;

import com.alikian.dto.UserDto;
import com.alikian.repository.UserRepository;
import com.alikian.service.ImportService;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ApplicationContextEvent;
import org.springframework.context.event.ContextStartedEvent;
import org.springframework.stereotype.Component;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

/**
 * Created by akian on 2/22/17.
 */
@Component
public class CStartEventHandler
    implements ApplicationListener<ApplicationReadyEvent> {

    @Autowired
    ImportService importService;

    @Override
    public void onApplicationEvent(ApplicationReadyEvent applicationReadyEvent) {
        importService.importData();
    }


}