package de.geroldbusch.helloworld;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    @Value("${greeting}")
    String greeting;

    @GetMapping
    public String hello(@RequestParam(defaultValue = "World") String name) {
        return greeting + " " + name + ".";
    }
}
