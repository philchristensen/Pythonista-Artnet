//
//  AppDelegate.m
//
//

#import "AppDelegate.h"
#import "PythonistaAppViewController.h"

@implementation AppDelegate

@synthesize window = _window;
@synthesize viewController = _viewController;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions 
{
	[[NSUserDefaults standardUserDefaults] setBool:YES forKey:kSettingScene32BitColors];
	[[NSUserDefaults standardUserDefaults] setBool:NO forKey:kSettingSceneAntialiasing];
		
	_window = self.window;
	
	NSString *bundledScriptPath = [[NSBundle mainBundle] pathForResource:@"Script" ofType:@"py"];
	NSString *docPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
	NSString *targetPath = [docPath stringByAppendingPathComponent:[bundledScriptPath lastPathComponent]];
	
	NSFileManager *fm = [NSFileManager defaultManager];
	NSDictionary *bundledFileAttributes = [fm attributesOfItemAtPath:bundledScriptPath error:NULL];
	NSDictionary *fileAttributes = [fm attributesOfItemAtPath:targetPath error:NULL];
	if (!fileAttributes || ![[bundledFileAttributes fileModificationDate] isEqualToDate:[fileAttributes fileModificationDate]]) {
		[fm removeItemAtPath:targetPath error:NULL];
		[fm copyItemAtPath:bundledScriptPath toPath:targetPath error:NULL];
	}
	
	_viewController = self.viewController = [[[PythonistaAppViewController alloc] initWithScriptPath:targetPath backgroundColor:[UIColor colorWithWhite:0.2 alpha:1.0] textColor:[UIColor colorWithWhite:0.9 alpha:1.0]] autorelease];
    
//    UIButton *infoButton = [UIButton buttonWithType:UIButtonTypeInfoLight];
//    [infoButton addTarget:self action:@selector(showControls) forControlEvents:UIControlEventTouchUpInside];

    UIBarButtonItem *controlsButton = [[[UIBarButtonItem alloc]
                                   initWithTitle:@"Controls"
                                   style:UIBarButtonItemStylePlain
                                   target:self
                                   action:@selector(showControls)] autorelease];

    
    self.viewController.navigationItem.rightBarButtonItem = controlsButton;
    
    [_window.rootViewController pushViewController:self.viewController animated:NO];
	
    [_window makeKeyAndVisible];
	return YES;
}

- (void) showControls {
    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"Storyboard" bundle:nil];
    UIViewController *vc = [storyboard instantiateViewControllerWithIdentifier:@"ControlsViewController"];
    
    [_window.rootViewController pushViewController:vc animated:YES];
}

- (void)dealloc
{
	[_viewController release];
	[_window release];
	[super dealloc];
}


@end
