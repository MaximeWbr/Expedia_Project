package com.mygdx.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.maps.tiled.TiledMap;
import com.badlogic.gdx.maps.tiled.TiledMapRenderer;
import com.badlogic.gdx.maps.tiled.TmxMapLoader;
import com.badlogic.gdx.maps.tiled.renderers.OrthoCachedTiledMapRenderer;

public class MyGdxGame /* Nom de la classe main du jeu */ extends ApplicationAdapter implements InputProcessor{
	TiledMap map; // map  
	OrthographicCamera camera; // camera
	TiledMapRenderer tiledMapRenderer; //Rendu de la map
	
	@Override
	//Fonction qui creer l'application lors du démarrage
	public void create () {
		float w = Gdx.graphics.getWidth();
		float h = Gdx.graphics.getHeight();
		camera = new OrthographicCamera(); //Creation de la camera
		camera.setToOrtho(false, w, h);	// Config de la camera
		camera.update();
		map = new TmxMapLoader().load("Magasin.tmx");	//Chargement de la map
		tiledMapRenderer = new OrthoCachedTiledMapRenderer(map); //Création du rendu de la map
		Gdx.input.setInputProcessor(this); // Mis en place des inputs 
	}

	@Override
	//Boucle infi, mais à jour l'application constamment
	public void render () {
		//Mise en place de la transparence entre les couches de la map
		Gdx.gl.glBlendFunc(GL20.GL_SRC_ALPHA, GL20.GL_ONE_MINUS_SRC_ALPHA);
		Gdx.gl20.glEnable(GL20.GL_BLEND);
		camera.update(); // Mise a jour de la camera
		tiledMapRenderer.setView(camera); // Affichage de la map en fonction de la camera
		tiledMapRenderer.render(); 

	}
	
	@Override
	public void dispose () {
	}

//Gestion des touches de clavier ... 
	@Override
	public boolean keyDown(int keycode) {
		return false;
	}

	@Override
	public boolean keyUp(int keycode) {
		if(keycode == Input.Keys.LEFT)
			camera.translate(-32,0);
		if(keycode == Input.Keys.RIGHT)
			camera.translate(32,0);
		if(keycode == Input.Keys.UP)
			camera.translate(0,-32);
		if(keycode == Input.Keys.DOWN)
			camera.translate(0,32);
		return false;
	}

	@Override
	public boolean keyTyped(char character) {
		return false;
	}

	@Override
	public boolean touchDown(int screenX, int screenY, int pointer, int button) {
		return false;
	}

	@Override
	public boolean touchUp(int screenX, int screenY, int pointer, int button) {
		return false;
	}

	@Override
	public boolean touchDragged(int screenX, int screenY, int pointer) {
		return false;
	}

	@Override
	public boolean mouseMoved(int screenX, int screenY) {
		return false;
	}

	@Override
	public boolean scrolled(int amount) {
		return false;
	}
	
}
